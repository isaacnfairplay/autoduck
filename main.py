import os
import time
from queue import Queue
from context_manager import load_context, save_context, update_system_prompt
from code_executor import SnippetBuilder
from api_client import generate_response, CodeSnippet, StringResponse
from git_handler import auto_commit_changes
from planning import parse_multi_step_task
from token_tracker import TokenTracker
from typing import Literal

VALID_CATEGORIES: tuple[Literal["connect"], Literal["query"], Literal["other"]] = ("connect", "query", "other")

# Ensure tasks directory exists
os.makedirs("tasks", exist_ok=True)

def process_task(task: str, builder: SnippetBuilder, context: dict, system_prompt: str, token_tracker: TokenTracker) -> str:
    steps = parse_multi_step_task(task)
    full_response = f"# Task: {task}\n\n"
    previous_code = "import duckdb\nduck_conn = duckdb.connect(':memory:')"
    valid, _ = builder.execute_snippet(previous_code)
    if not valid:
        return "Error: Could not initialize DuckDB connection"
    builder.store_snippet("connect", previous_code, None, True, builder.get_variable_info(previous_code))

    for i, step in enumerate(steps, 1):
        print(f"Processing step {i}: {step}")
        max_attempts = 3
        for attempt in range(max_attempts):
            prompt = f"Previous code:\n{previous_code}\nTask: {step}\nGenerate a Python code snippet using DuckDB."
            try:
                response = generate_response(prompt, system_prompt, token_tracker, max_tokens=500, response_model=CodeSnippet, retries=3)
                if not isinstance(response, CodeSnippet):
                    raise ValueError("Expected CodeSnippet, got TaskList")
                code_snippet = response.code
            except Exception as e:
                full_response += f"## Step {i}: {step}\n\nError generating code: {e}\n"
                break
            if not code_snippet:
                full_response += f"## Step {i}: {step}\n\nNo code generated\n"
                break
            valid, result = builder.execute_snippet(code_snippet)
            if valid:
                vars_info = builder.get_variable_info(code_snippet)
                category: Literal["connect", "query", "other"] = "query" if "SELECT" in code_snippet.upper() else "other"
                builder.store_snippet(category, code_snippet, result, True, vars_info)
                auto_commit_changes(f"Added snippet for step {i} of task: {step}")
                full_response += f"## Step {i}: {step}\n\n```python\n{code_snippet}\n```\n\n**Result**: {result}"
                if response.explanation:
                    full_response += f"\n\n**Explanation**: {response.explanation}"
                full_response += "\n"
                previous_code += f"\n{code_snippet}"
                break
            elif attempt < max_attempts - 1:
                prompt = f"Previous code:\n{previous_code}\nCode:\n{code_snippet}\nError: {result}\nFix this code."
            else:
                full_response += f"## Step {i}: {step}\n\nFailed after {max_attempts} attempts: {result}\n"
    return full_response

def main():
    builder = SnippetBuilder()
    task_queue = Queue()
    system_prompt = open("system_prompt.txt").read()
    token_tracker = TokenTracker()  # Single instance for the session
    print("Initialized")

    while True:
        try:
            # Reload .env limits before each iteration
            token_tracker.reload_limits()
            context = load_context()
            print(f"Loaded context with {len(context.get('completed_tasks', []))} completed tasks")
            if task_queue.empty():
                # Construct Mega prompt with all context
                completed_tasks_str = "\n".join(f"- {task}" for task in context.get("completed_tasks", []))
                current_issues_str = "\n".join(f"- {issue}" for issue in context.get("current_issues", []))
                goals_str = "\n".join(f"- {goal}" for goal in context.get("goals", []))
                mega_prompt = (
                    f"Completed Tasks:\n{completed_tasks_str or 'None'}\n\n"
                    f"Current Issues:\n{current_issues_str or 'None'}\n\n"
                    f"Goals:\n{goals_str or 'None'}\n\n"
                    "Please provide the next task or feedback. If you want to update the system prompt, "
                    "start your response with 'UPDATE PROMPT:' followed by the new instruction."
                )
                print("Generating next task via Mega prompt...")
                response = generate_response(mega_prompt, system_prompt, token_tracker, max_tokens=500, response_model=StringResponse, retries=3)
                reply = response.response.strip()
                print(f"Received reply: {reply}")
                if reply.startswith("UPDATE PROMPT:"):
                    instruction = reply[len("UPDATE PROMPT:"):].strip()
                    update_system_prompt(instruction, "user requested via Mega prompt", context)
                    print(f"Updated system prompt with: {instruction}")
                else:
                    task_queue.put(reply)
                    print(f"Added task to queue: {reply}")
            while not task_queue.empty():
                task = task_queue.get()
                print(f"Processing task: {task}")
                full_response = process_task(task, builder, context, system_prompt, token_tracker)
                # Generate markdown file for the task
                task_seq = len(os.listdir("tasks"))
                filename = f"tasks/task_{task_seq:03d}.md"
                with open(filename, "w") as f:
                    f.write(full_response)
                print(f"Saved task output to {filename}")
                context.setdefault("completed_tasks", []).append(task)
                save_context(context)
                task_queue.task_done()
                print(f"Completed task: {task}")
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
            time.sleep(60)  # Wait 60 seconds

if __name__ == "__main__":
    main()