import os
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.utils import parsedate_to_datetime
from typing import Optional
import json
import time
from datetime import datetime
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

# Email configuration
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
USER_EMAIL = os.getenv("USER_EMAIL")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")
PROCESSED_EMAILS_FILE = "processed_emails.json"

def generate_session_id() -> str:
    """Generate a unique session ID for email tracking."""
    return f"SESSION-{datetime.now().strftime('%Y%m%d%H%M')}"

def send_email(subject: str, body: str, to_email: str) -> float:
    """Send an email and return the timestamp of sending."""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    sent_time = time.time()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
    logger.info(f"Email sent to {to_email} with subject: {subject}")
    return sent_time

def load_processed_emails() -> list[str]:
    """Load the list of processed email message IDs."""
    if not os.path.exists(PROCESSED_EMAILS_FILE):
        return []
    with open(PROCESSED_EMAILS_FILE, "r") as f:
        return json.load(f)

def save_processed_email(message_id: str) -> None:
    """Save a processed email message ID to avoid reprocessing."""
    processed = load_processed_emails()
    if message_id not in processed:
        processed.append(message_id)
        with open(PROCESSED_EMAILS_FILE, "w") as f:
            json.dump(processed, f)

def get_email_input(session_id: str, from_email: str, sent_time: float, timeout: int = 86400) -> str:
    """Retrieve a reply email matching the session ID and sender."""
    processed = load_processed_emails()
    with imaplib.IMAP4_SSL(IMAP_SERVER) as mail:
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        end_time = time.time() + timeout
        while time.time() < end_time:
            mail.select("inbox")
            status, data = mail.search(None, f"{session_id}")
            if status != "OK" or not data[0]:
                time.sleep(15)
                continue
            email_ids = data[0].split()
            for email_id in reversed(email_ids):
                status, msg_data = mail.fetch(email_id, "(RFC822)")
                if status != "OK":
                    continue
                msg = email.message_from_bytes(msg_data[0][1])
                sender = msg.get("From", "")
                message_id = msg.get("Message-ID", f"unknown-{email_id}")
                if message_id in processed:
                    continue
                email_time = parsedate_to_datetime(msg.get("Date", "Unknown")).timestamp()
                if email_time < sent_time or from_email not in sender or session_id not in msg.get("Subject", ""):
                    continue
                save_processed_email(message_id)
                return (msg.get_payload(decode=True).decode().strip() if not msg.is_multipart() else
                        next((part.get_payload(decode=True).decode().strip() for part in msg.walk()
                              if part.get_content_type() == "text/plain"), ""))
            time.sleep(15)
        return ""

if __name__ == "__main__":
    # Test session ID generation
    print(f"Generated Session ID: {generate_session_id()}")
    # Test email sending
    send_email("Test Subject", "Test Body", USER_EMAIL)
    # Test email retrieval (requires a sent email with a session ID)
    session_id = generate_session_id()
    sent_time = send_email(f"Test [{session_id}]", "Please reply", USER_EMAIL)
    print(f"Waiting for reply with session ID {session_id}...")
    reply = get_email_input(session_id, USER_EMAIL, sent_time, timeout=30)
    print(f"Reply: {reply}")