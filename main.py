import time
from queue import Queue
import logging
from email_handler import send_email, get_email_input, generate_session_id
from context_manager import load_context, save_context, update_system_prompt
from code_executor import SnippetBuilder
from api_client import generate_response, extract_code
from git_handler import auto_commit_changes
from planning import generate_tasks, parse_multi_step_task
from logging_config import setup_logging

logger = setup_logging()

def process_task(task: str, builder: SnippetBuilder, context: dict, session_id: str, system_prompt: str) -> str:
    steps = parse_multi_step_task(task)
    full_response = ""
    previous_code = "import duckdb\nduck_conn = duckdb.connect(':memory:')"
    valid, _ = builder.execute_snippet(previous_code)
    if not valid:
        return "Error: Could not initialize DuckDB connection"
    builder.store_snippet("task_init", previous_code, None, True, builder.get_variable_info(previous_code))

    for i, step in enumerate(steps, 1):
        logger.info(f"Processing step {i}: {step}")
        max_attempts = 3
        for attempt in range(max_attempts):
            prompt = f"Previous code:\n```python\n{previous_code}\n```\nTask: {step}\nGenerate a Python code snippet using DuckDB."
            response = generate_response(prompt, system_prompt)
            code_snippet = extract_code(response)
            if not code_snippet:
                full_response += f"\nStep {i}: {step}\nNo code generated\n"
                break
            valid, result = builder.execute_snippet(code_snippet)
            if valid:
                vars_info = builder.get_variable_info(code_snippet)
                builder.store_snippet(f"task_step_{i}", code_snippet, result, True, vars_info)
                auto_commit_changes(f"Added snippet for step {i} of task: {step}")
                full_response += f"\nStep {i}: {step}\n```python\n{code_snippet}\n```\nResult: {result}"
                previous_code += f"\n{code_snippet}"
                break
            elif attempt < max_attempts - 1:
                prompt = f"Fix this code:\n```python\n{code_snippet}\n```\nError: {result}"
                response = generate_response(prompt, system_prompt)
                code_snippet = extract_code(response)
            else:
                full_response += f"\nStep {i}: {step}\nFailed after {max_attempts} attempts: {result}\n"
    return full_response

def main():
    builder = SnippetBuilder()
    task_queue = Queue()
    current_session_id = None
    last_task_time = 0
    system_prompt = open("system_prompt.txt").read()

    while True:
        try:
            context = load_context()
            if task_queue.empty():
                if not current_session_id or time.time() - last_task_time > 86400:
                    current_session_id = generate_session_id()
                subject = f"DuckDB Documentation Task Request [{current_session_id}]"
                
                sent_time = send_email(subject, "Please provide the next task or feedback.", os.getenv("USER_EMAIL"))
                reply = get_email_input(current_session_id, os.getenv("USER_EMAIL"), sent_time)
                
                if not reply:
                    logger.info("No reply received, generating tasks automatically.")
                    tasks = generate_tasks(context, system_prompt)
                    for task in tasks:
                        task_queue.put(task)
                elif "UPDATE PROMPT:" in reply:
                    instruction = reply.split("UPDATE PROMPT:")[1].strip()
                    update_system_prompt(instruction, "user requested via email", context)
                    send_email(subject, "Prompt updated.", os.getenv("USER_EMAIL"))
                    auto_commit_changes("Updated system prompt")
                else:
                    task_queue.put(reply.strip())

            while not task_queue.empty():
                task = task_queue.get()
                full_response = process_task(task, builder, context, current_session_id, system_prompt)
                send_email(subject, full_response, os.getenv("USER_EMAIL"))
                context["completed_tasks"].append(task)
                save_context(context)
                last_task_time = time.time()
                task_queue.task_done()

        except Exception as e:
            logger.error(f"Error: {e}")
            send_email(f"Error [{current_session_id}]", str(e), os.getenv("USER_EMAIL"))
            time.sleep(3600)

if __name__ == "__main__":
    main()