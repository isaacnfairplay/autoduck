import os
import logging
import sys
from dotenv import load_dotenv

load_dotenv()

def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # Set level directly
    
    SENSITIVE_DATA = {
        os.getenv("EMAIL_ADDRESS"): "[EMAIL_ADDRESS]",
        os.getenv("EMAIL_PASSWORD"): "[EMAIL_PASSWORD]",
        os.getenv("USER_EMAIL"): "[USER_EMAIL]",
        os.getenv("ANTHROPIC_API_KEY"): "[API_KEY]"
    }
    
    class AnonymizingHandler(logging.StreamHandler):
        def __init__(self):
            super().__init__(stream=sys.stdout)
            self.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        
        def emit(self, record):
            record.msg = anonymize_log(str(record.msg))
            super().emit(record)
    
    def anonymize_log(message: str) -> str:
        for sensitive, placeholder in SENSITIVE_DATA.items():
            if sensitive and sensitive in message:
                message = message.replace(sensitive, placeholder)
        return message
    
    logger.handlers = [AnonymizingHandler()]
    return logger

if __name__ == "__main__":
    logger = setup_logging()
    logger.info(f"Testing with sensitive data: {os.getenv('EMAIL_ADDRESS')}")
    logger.error("Test error message")