import subprocess
import logging

logger = logging.getLogger(__name__)

def auto_commit_changes(commit_message: str) -> None:
    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)
        # Check if there are changes to commit
        result = subprocess.run(["git", "diff", "--cached", "--quiet"], check=False)
        if result.returncode != 0:
            # Commit the changes
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            logger.info(f"Changes committed: {commit_message}")
            # Push to remote repository
            subprocess.run(["git", "push"], check=True)
            logger.info("Changes pushed to remote repository")
        else:
            logger.info("No changes to commit.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to commit or push changes: {e}")

if __name__ == "__main__":
    auto_commit_changes("Test commit from git_handler")