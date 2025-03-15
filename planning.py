import re
from api_client import generate_response
from context_manager import load_context

def generate_tasks(context: dict, system_prompt: str, num_tasks: int = 3) -> list[str]:
    """Generate a list of tasks based on context."""
    context_str = f"Completed tasks: {', '.join(context['completed_tasks'])}\nIssues: {', '.join(context['current_issues'])}\nGoals: {', '.join(context['goals'])}"
    prompt = f"Given the current context: {context_str}, suggest {num_tasks} next tasks for DuckDB documentation."
    response = generate_response(prompt, system_prompt, max_tokens=150)
    return [task.strip() for task in response.split('\n') if task.strip()]

def parse_multi_step_task(task: str) -> list[str]:
    """Parse a task into individual steps."""
    steps = []
    if "Step" in task:
        for line in task.split('\n'):
            if line.strip().startswith("Step"):
                steps.append(line.strip().split(":", 1)[1].strip())
    else:
        steps = [step.strip() for step in task.split(';') if step.strip()]
    return steps if steps else [task]

if __name__ == "__main__":
    context = load_context()
    system_prompt = open("system_prompt.txt").read()
    tasks = generate_tasks(context, system_prompt)
    print("Generated Tasks:", tasks)
    test_task = "Step 1: Create table; Step 2: Query data"
    print("Parsed Steps:", parse_multi_step_task(test_task))