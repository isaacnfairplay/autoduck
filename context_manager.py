import json
import os
from datetime import datetime
from typing import Optional
from api_client import generate_response

CONTEXT_FILE = "context.json"
SYSTEM_PROMPT_FILE = "system_prompt.txt"

def load_context() -> dict:
    """Load the context from file or initialize with defaults."""
    if not os.path.exists(CONTEXT_FILE):
        default = {"completed_tasks": [], "current_issues": [], "goals": ["create comprehensive DuckDB documentation"], "additional_instructions": []}
        with open(CONTEXT_FILE, "w") as f:
            json.dump(default, f, indent=2)
        return default
    with open(CONTEXT_FILE, "r") as f:
        return json.load(f)

def save_context(context: dict) -> None:
    """Save the context to file."""
    with open(CONTEXT_FILE, "w") as f:
        json.dump(context, f, indent=2)

def update_system_prompt(new_instruction: str, reason: str, context: dict) -> None:
    """Update the system prompt with a refined instruction."""
    if not os.path.exists(SYSTEM_PROMPT_FILE):
        with open(SYSTEM_PROMPT_FILE, "w") as f:
            f.write("You are an AI assistant helping with DuckDB documentation.")
    system_prompt = open(SYSTEM_PROMPT_FILE).read()
    context_str = f"Completed tasks: {', '.join(context['completed_tasks'])}\nIssues: {', '.join(context['current_issues'])}\nGoals: {', '.join(context['goals'])}"
    prompt = f"Current context: {context_str}\nUser requested instruction: '{new_instruction}'\nRefine this into a concise directive."
    refined = generate_response(prompt, system_prompt, max_tokens=50)
    with open(SYSTEM_PROMPT_FILE, "a") as f:
        f.write(f"\n{refined} [Added on {datetime.now().strftime('%Y-%m-%d %H:%M')} because {reason}.]")

if __name__ == "__main__":
    context = load_context()
    print(f"Initial Context: {context}")
    update_system_prompt("Focus on advanced queries", "test update", context)
    context["completed_tasks"].append("Test task")
    save_context(context)
    print(f"Updated Context: {load_context()}")