import os
import re
from api_client import generate_response
from context_manager import load_context

def generate_tasks(context: dict, system_prompt: str, num_tasks: int = 3) -> list[str]:
    context_str = f"Completed tasks: {', '.join(context['completed_tasks'])}\nIssues: {', '.join(context['current_issues'])}\nGoals: {', '.join(context['goals'])}"
    prompt = f"Given the current context: {context_str}, suggest {num_tasks} next tasks for DuckDB documentation."
    response = generate_response(prompt, system_prompt, max_tokens=150)
    return [task.strip() for task in response.split('\n') if task.strip()]

def parse_multi_step_task(task: str) -> list[str]:
    steps = []
    # Split by newlines and process each line
    lines = task.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith("Step"):
            try:
                step_content = line.split(":", 1)[1].strip()
                steps.append(step_content)
            except IndexError:
                continue
        elif ';' in line:
            # Handle semicolon-separated steps within a line
            sub_steps = [s.strip() for s in line.split(';') if s.strip()]
            steps.extend(sub_steps)
    # If no steps were found, treat the entire task as a single step
    return steps if steps else [task.strip()]

if __name__ == "__main__":
    context = load_context()
    system_prompt = open("system_prompt.txt").read()
    if os.getenv("ANTHROPIC_API_KEY"):
        tasks = generate_tasks(context, system_prompt)
        print("Generated Tasks:", tasks)
    else:
        print("Skipping task generation: ANTHROPIC_API_KEY missing in .env")
    test_task = "Step 1: Create table; Step 2: Query data"
    print("Parsed Steps:", parse_multi_step_task(test_task))