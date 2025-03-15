import os
import json
import re
import traceback
import subprocess
import logging
from datetime import datetime
import time
from dotenv import load_dotenv
import anthropic
import duckdb
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.utils import parsedate_to_datetime
from typing import Any, Optional, Literal
from typing_extensions import TypeAlias
from queue import Queue

# Setup logging with anonymization
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

load_dotenv()

SnippetResult: TypeAlias = tuple[bool, Optional[str]]
VarInfo: TypeAlias = dict[str, str]
Category: TypeAlias = Literal["connect", "query", "other"]

# Email configuration
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # Gmail for sending/receiving
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
USER_EMAIL = os.getenv("USER_EMAIL")       # ProtonMail for correspondence
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")

SENSITIVE_DATA = {
    EMAIL_ADDRESS: "[EMAIL_ADDRESS]",
    EMAIL_PASSWORD: "[EMAIL_PASSWORD]",
    USER_EMAIL: "[USER_EMAIL]",
    os.getenv("ANTHROPIC_API_KEY"): "[API_KEY]"
}

def anonymize_log(message: str) -> str:
    for sensitive, placeholder in SENSITIVE_DATA.items():
        if sensitive and sensitive in message:
            message = message.replace(sensitive, placeholder)
    return message

class AnonymizingHandler(logging.StreamHandler):
    def emit(self, record):
        record.msg = anonymize_log(str(record.msg))
        super().emit(record)

logger.handlers = [AnonymizingHandler()]

if not EMAIL_ADDRESS or not EMAIL_PASSWORD or not USER_EMAIL:
    raise ValueError("Missing EMAIL_ADDRESS, EMAIL_PASSWORD, or USER_EMAIL in .env file.")

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY not found in .env file.")
model = os.getenv("ANTHROPIC_MODEL", "claude-3-5-haiku-20241022")
client = anthropic.Anthropic(api_key=api_key)

CONTEXT_FILE = "context.json"
SYSTEM_PROMPT_FILE = "system_prompt.txt"
SNIPPET_DIR = "generated_snippets"
PROCESSED_EMAILS_FILE = "processed_emails.json"
os.makedirs(SNIPPET_DIR, exist_ok=True)

if not os.path.exists(CONTEXT_FILE):
    with open(CONTEXT_FILE, "w") as f:
        json.dump({"completed_tasks": [], "current_issues": [], "goals": ["create comprehensive DuckDB documentation"], "additional_instructions": []}, f, indent=2)

if not os.path.exists(SYSTEM_PROMPT_FILE):
    with open(SYSTEM_PROMPT_FILE, "w") as f:
        f.write("You are an AI assistant helping with DuckDB documentation by generating and testing valid Python code examples using DuckDB objects.")

if not os.path.exists(PROCESSED_EMAILS_FILE):
    with open(PROCESSED_EMAILS_FILE, "w") as f:
        json.dump([], f)

def generate_session_id() -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    return f"SESSION-{timestamp}"

def send_email(subject: str, body: str, to_email: str) -> float:
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        sent_time = time.time()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        logger.info(f"Email sent from [EMAIL_ADDRESS] to [USER_EMAIL] with subject: {subject}")
        return sent_time
    except Exception as e:
        logger.error(f"Failed to send email from [EMAIL_ADDRESS] to [USER_EMAIL]: {e}")
        return time.time()

def load_processed_emails() -> list[str]:
    with open(PROCESSED_EMAILS_FILE, "r") as f:
        return json.load(f)

def save_processed_email(message_id: str) -> None:
    processed = load_processed_emails()
    if message_id not in processed:
        processed.append(message_id)
        with open(PROCESSED_EMAILS_FILE, "w") as f:
            json.dump(processed, f)

def get_email_input(session_id: str, from_email: str, sent_time: float, timeout: int = 86400) -> str:
    processed = load_processed_emails()
    try:
        with imaplib.IMAP4_SSL(IMAP_SERVER) as mail:
            mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            end_time = time.time() + timeout
            while time.time() < end_time:
                mail.select("inbox")
                mail.noop()
                status, data = mail.search(None, f"{session_id}")  # Search for session_id
                if status != "OK":
                    logger.error(f"IMAP search failed for [EMAIL_ADDRESS]: {data}")
                    time.sleep(15)
                    continue
                if not data[0]:
                    logger.debug(f"No emails found with session ID {session_id}")
                    time.sleep(15)
                    continue
                email_ids = data[0].split()
                for email_id_num in reversed(email_ids):  # Check all matching emails, newest first
                    status, msg_data = mail.fetch(email_id_num, "(RFC822)")
                    if status != "OK":
                        continue
                    raw_email = msg_data[0][1]
                    msg = email.message_from_bytes(raw_email)
                    sender = msg.get("From", "")
                    subject = msg.get("Subject", "")
                    date_str = msg.get("Date", "Unknown")
                    message_id = msg.get("Message-ID", f"unknown-{email_id_num}")
                    if message_id in processed:
                        continue
                    email_time = parsedate_to_datetime(date_str).timestamp() if date_str != "Unknown" else 0
                    if email_time < sent_time:
                        logger.debug(f"Skipping email before sent time: {subject} (Date: {date_str})")
                        continue
                    logger.info(f"Checking email subject: {subject} (Date: {date_str})")
                    if from_email in sender and session_id in subject:
                        logger.info(f"Found reply from [USER_EMAIL] with session ID {session_id}")
                        save_processed_email(message_id)
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    return part.get_payload(decode=True).decode().strip()
                        else:
                            return msg.get_payload(decode=True).decode().strip()
                logger.info(f"No matching reply found yet for session ID {session_id}")
                time.sleep(15)
            logger.info(f"Timeout reached for session ID {session_id}, no reply received.")
            return ""
    except Exception as e:
        logger.error(f"IMAP error for [EMAIL_ADDRESS]: {e}\n{anonymize_log(traceback.format_exc())}")
        return ""

def load_context() -> dict:
    with open(CONTEXT_FILE, "r") as f:
        return json.load(f)

def save_context(context: dict) -> None:
    with open(CONTEXT_FILE, "w") as f:
        json.dump(context, f, indent=2)

def update_system_prompt(new_instruction: str, reason: str, context: dict) -> None:
    system_prompt = open(SYSTEM_PROMPT_FILE).read()
    context_str = (f"Completed tasks: {', '.join(context['completed_tasks'])}\n"
                   f"Issues: {', '.join(context['current_issues'])}\n"
                   f"Goals: {', '.join(context['goals'])}")
    user_message = (f"Current context: {context_str}\n"
                    f"User requested instruction: '{new_instruction}'\n"
                    "Refine this into a concise directive for DuckDB documentation.")
    response = client.messages.create(
        model=model,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
        max_tokens=50
    )
    refined_instruction = response.content[0].text.strip()
    with open(SYSTEM_PROMPT_FILE, "a") as f:
        f.write(f"\n{refined_instruction} [Added on {datetime.now().strftime('%Y-%m-%d %H:%M')} because {reason}.]")

def generate_response(task: str, context: dict, previous_code: str = "") -> str:
    system_prompt = open(SYSTEM_PROMPT_FILE).read()
    context_str = (f"Completed tasks: {', '.join(context['completed_tasks'])}\n"
                   f"Issues: {', '.join(context['current_issues'])}\n"
                   f"Goals: {', '.join(context['goals'])}")
    user_message = (f"Current context: {context_str}\n"
                    f"Previous code:\n```python\n{previous_code}\n```\n"
                    f"Task: {task}\n"
                    "Generate a valid Python code snippet using DuckDB objects that builds on the previous code.")
    response = client.messages.create(
        model=model,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
        max_tokens=100
    )
    return response.content[0].text.strip()

def fix_code_snippet(snippet: str, error: str, context: dict, previous_code: str = "") -> str:
    system_prompt = open(SYSTEM_PROMPT_FILE).read()
    context_str = (f"Completed tasks: {', '.join(context['completed_tasks'])}\n"
                   f"Issues: {', '.join(context['current_issues'])}\n"
                   f"Goals: {', '.join(context['goals'])}")
    user_message = (f"Current context: {context_str}\n"
                    f"Previous code:\n```python\n{previous_code}\n```\n"
                    f"Code snippet:\n```python\n{snippet}\n```\n"
                    f"Error: {error}\n"
                    "Fix this code to be valid Python using DuckDB objects.")
    response = client.messages.create(
        model=model,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
        max_tokens=100
    )
    return response.content[0].text.strip()

def generate_email_request(context: dict) -> str:
    system_prompt = open(SYSTEM_PROMPT_FILE).read()
    context_str = (f"Completed tasks: {', '.join(context['completed_tasks'])}\n"
                   f"Issues: {', '.join(context['current_issues'])}\n"
                   f"Goals: {', '.join(context['goals'])}")
    user_message = (f"Current context: {context_str}\n"
                    "Ask for the next DuckDB task or feedback, short and professional.")
    response = client.messages.create(
        model=model,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
        max_tokens=50
    )
    return response.content[0].text.strip()

def extract_code(response: str) -> str:
    match = re.search(r"```python(.*?)```", response, re.DOTALL)
    return match.group(1).strip() if match else response.strip()

def auto_commit_changes(commit_message: str) -> None:
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "reset", "core.py"], check=True)
        result = subprocess.run(["git", "diff", "--cached", "--quiet"], check=False)
        if result.returncode != 0:
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            logger.info(f"Changes committed: {commit_message}")
        else:
            logger.info("No changes to commit.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to commit changes: {e}")

class SnippetBuilder:
    def __init__(self) -> None:
        self.context: dict[str, Any] = {}
        self.conn: Optional[duckdb.DuckDBPyConnection] = None
        self.prev_vars: set[str] = set()

    def execute_snippet(self, snippet: str) -> SnippetResult:
        if not snippet.strip():
            return False, "Empty snippet"
        try:
            exec(snippet, self.context)
            if "conn" in self.context and not self.conn:
                self.conn = self.context["conn"]
            result = self.context.get("result")
            return True, str(result) if result else None
        except Exception as e:
            return False, str(e)

    def get_variable_info(self, snippet: str) -> VarInfo:
        new_vars: VarInfo = {}
        current_vars = set(self.context.keys())
        added_vars = current_vars - self.prev_vars
        for var in added_vars:
            obj = self.context[var]
            var_type = type(obj).__name__
            details = f"Type: {var_type}"
            if isinstance(obj, duckdb.DuckDBPyRelation):
                details += "\nAttributes: .query(), .columns, .fetchall()"
            elif isinstance(obj, duckdb.DuckDBPyConnection):
                details += "\nAttributes: .execute(), .close()"
            new_vars[var] = details
        self.prev_vars = current_vars
        return new_vars

    def store_snippet(self, category: Category, snippet: str, result: Optional[str], valid: bool, vars_info: VarInfo) -> str:
        seq = len([f for f in os.listdir(SNIPPET_DIR) if f.startswith(category)])
        filename = f"{SNIPPET_DIR}/{category}_{seq:03d}.py"
        with open(filename, "w") as f:
            f.write(f"# Generated: {datetime.now()}\n# Result: {result}\n# Valid: {valid}\n")
            for var, info in vars_info.items():
                f.write(f"# Variable {var}: {info}\n")
            f.write(snippet)
        context = load_context()
        context["completed_tasks"].append(category)
        save_context(context)
        return filename

def parse_multi_step_task(task: str) -> list[str]:
    steps = []
    if "Step" in task:
        for line in task.split('\n'):
            if line.strip().startswith("Step"):
                steps.append(line.strip().split(":", 1)[1].strip())
    else:
        steps = [step.strip() for step in task.split(';') if step.strip()]
    return steps if steps else [task]

def process_task(task: str, builder: 'SnippetBuilder', context: dict, session_id: str) -> str:
    steps = parse_multi_step_task(task)
    full_response = ""
    previous_code = "duck_conn = duckdb.connect(':memory:')"
    valid, _ = builder.execute_snippet(previous_code)
    if not valid:
        logger.error("Failed to initialize DuckDB connection")
        return "Error: Could not initialize DuckDB connection"
    builder.store_snippet("task_init", previous_code, None, True, builder.get_variable_info(previous_code))

    for i, step in enumerate(steps, 1):
        logger.info(f"Processing step {i}: {step}")
        max_attempts = 3
        for attempt in range(max_attempts):
            response = generate_response(step, context, previous_code)
            code_snippet = extract_code(response)
            if not code_snippet:
                full_response += f"\nStep {i}: {step}\nNo code generated\n"
                break
            valid, result = builder.execute_snippet(code_snippet)
            if valid:
                vars_info = builder.get_variable_info(code_snippet)
                builder.store_snippet(f"task_step_{i}", code_snippet, result, True, vars_info)
                commit_message = f"Added valid snippet for step {i} of task: {step}"
                auto_commit_changes(commit_message)
                full_response += (f"\nStep {i}: {step}\n"
                                 f"```python\n{code_snippet}\n```\nResult: {result}")
                previous_code += f"\n{code_snippet}"
                break
            else:
                logger.info(f"Attempt {attempt + 1} failed for step {i}: {result}")
                if attempt < max_attempts - 1:
                    code_snippet = fix_code_snippet(code_snippet, result, context, previous_code)
                else:
                    full_response += f"\nStep {i}: {step}\nFailed after {max_attempts} attempts: {result}\n"
                    commit_message = f"Failed to fix snippet for step {i} of task: {step}"
                    auto_commit_changes(commit_message)
    return full_response

def parse_email_for_update(email_body: str, context: dict) -> None:
    if "UPDATE PROMPT:" in email_body:
        instruction = email_body.split("UPDATE PROMPT:")[1].strip()
        update_system_prompt(instruction, "user requested via email", context)

def main() -> None:
    builder = SnippetBuilder()
    task_queue = Queue()
    current_session_id = None
    last_task_time = 0
    while True:
        try:
            if task_queue.empty():
                if not current_session_id or time.time() - last_task_time > 86400:
                    current_session_id = generate_session_id()
                    sent_time = time.time()
                subject = f"DuckDB Documentation Task Request [{current_session_id}]"
                context = load_context()
                body = generate_email_request(context)
                sent_time = send_email(subject, body, USER_EMAIL)
                logger.info(f"Sent email with session ID {current_session_id}, waiting for reply...")
                
                reply = get_email_input(current_session_id, USER_EMAIL, sent_time, timeout=86400)
                if not reply:
                    logger.info("No reply received within 24 hours, sending reminder.")
                    reminder_body = generate_email_request(context)
                    sent_time = send_email(subject, f"Reminder: {reminder_body}", USER_EMAIL)
                    time.sleep(86400)
                    continue

                if "NEW CHAIN:" in reply:
                    current_session_id = generate_session_id()
                    sent_time = time.time()
                    reply = reply.split("NEW CHAIN:")[1].strip()
                    logger.info(f"Starting new session with ID {current_session_id}")
                
                if "UPDATE PROMPT:" in reply:
                    parse_email_for_update(reply, context)
                    send_email(subject, "Prompt updated.", USER_EMAIL)
                    auto_commit_changes("Updated system prompt based on user feedback")
                else:
                    current_task = reply.strip()
                    context = load_context()
                    full_response = process_task(current_task, builder, context, current_session_id)
                    send_email(subject, full_response, USER_EMAIL)
                    last_task_time = time.time()

            while not task_queue.empty():
                task = task_queue.get()
                context = load_context()
                full_response = process_task(task, builder, context, current_session_id)
                send_email(subject, full_response, USER_EMAIL)
                task_queue.task_done()

        except Exception as e:
            error_message = f"Error: {str(e)}"
            logger.error(error_message)
            send_email(f"Error in DuckDB Task [{current_session_id}]", error_message, USER_EMAIL)
            commit_message = f"Handled error for task: {current_task if 'current_task' in locals() else 'unknown'}"
            auto_commit_changes(commit_message)
            time.sleep(3600)

if __name__ == "__main__":
    main()
