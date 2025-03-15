import subprocess
import logging

logger = logging.getLogger(__name__)

def auto_commit_changes(commit_message: str) -> None:
    try:
        subprocess.run(["git", "add", "."], check=True)
        result = subprocess.run(["git", "diff", "--cached", "--quiet"], check=False)
        if result.returncode != 0:
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            logger.info(f"Changes committed: {commit_message}")
        else:
            logger.info("No changes to commit.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to commit changes: {e}")

if __name__ == "__main__":
    auto_commit_changes("Test commit from git_handler")