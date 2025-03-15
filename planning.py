import os
import re
from api_client import generate_response
from context_manager import load_context

def generate_tasks(context: dict, system_prompt: str, num_tasks: int = 3) -> list[str]:
    context_str = f"Completed tasks: {', '.join(context['completed_tasks'])}\nIssues: {', '.join(context['current_issues'])}\nGoals: {', '.join(context['goals'])}"
    prompt = f"Given the current context: {context_str}, suggest {num_tasks} next tasks for DuckDB documentation."
    response = generate_response(prompt, system_prompt, max_tokens=500)
    return [task.strip() for task in response.split('\n') if task.strip()]

def parse_multi_step_task(task: str) -> list[str]:
    steps = []
    # Split by newlines
    lines = task.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Match "Step X: " pattern and extract content
        step_matches = re.findall(r'Step \d+:\s*(.+?)(?=(?:Step \d+:|$))', line, re.DOTALL)
        if step_matches:
            for match in step_matches:
                # Split by semicolons within each step content
                sub_steps = [s.strip() for s in match.split(';') if s.strip()]
                steps.extend(sub_steps)
        elif ';' in line:
            # Handle plain semicolon-separated steps
            steps.extend(s.strip() for s in line.split(';') if s.strip())
        else:
            steps.append(line)
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