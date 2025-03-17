import os
from api_client import generate_response, TaskList
from context_manager import load_context
from typing import List
import re

def generate_tasks(context: dict, system_prompt: str, num_tasks: int = 3) -> List[str]:
    context_str = f"Completed tasks: {', '.join(context['completed_tasks'])}\nIssues: {', '.join(context['current_issues'])}\nGoals: {', '.join(context['goals'])}"
    prompt = (
        f"Given the current context: {context_str}, suggest {num_tasks} next tasks for DuckDB documentation.\n"
        "Respond ONLY with a valid JSON object containing a 'tasks' array, where each task has a 'description' field. "
        "Do not include any text, Markdown, or code blocks outside the JSON structure."
    )
    response = generate_response(prompt, system_prompt, max_tokens=500, response_model=TaskList)
    return [task.description for task in response.tasks]

def parse_multi_step_task(task: str) -> List[str]:
    steps = []
    lines = task.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if "Step" in line:
            step_matches = re.findall(r'Step \d+:\s*(.+?)(?=(?:Step \d+:|$))', line, re.DOTALL)
            for match in step_matches:
                sub_steps = [s.strip() for s in match.split(';') if s.strip()]
                steps.extend(sub_steps)
        elif ';' in line:
            steps.extend(s.strip() for s in line.split(';') if s.strip())
        else:
            steps.append(line)
    return steps if steps else [task.strip()]

if __name__ == "__main__":
    context = load_context()
    system_prompt = open("system_prompt.txt").read()
    if os.getenv("ANTHROPIC_API_KEY"):
        try:
            tasks = generate_tasks(context, system_prompt)
            print("Generated Tasks:", tasks)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Skipping task generation: ANTHROPIC_API_KEY missing in .env")
    test_task = "Step 1: Create table; Step 2: Query data"
    print("Parsed Steps:", parse_multi_step_task(test_task))