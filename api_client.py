import os
import anthropic
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Union, Type
import json
import re

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
MODEL = os.getenv("ANTHROPIC_MODEL", "claude-3-5-haiku-20241022")

# Define Pydantic models for structured responses
class CodeSnippet(BaseModel):
    code: str = Field(description="The Python code snippet")
    explanation: Optional[str] = Field(default=None, description="Explanation of the code")

class Task(BaseModel):
    description: str = Field(description="Description of the task")

class TaskList(BaseModel):
    tasks: list[Task] = Field(description="List of suggested tasks")

def generate_response(prompt: str, system_prompt: str, max_tokens: int = 500, response_model: Type[Union[CodeSnippet, TaskList]] = CodeSnippet) -> Union[CodeSnippet, TaskList]:
    """Generate a structured JSON response based on the expected model."""
    full_prompt = (
        f"{system_prompt}\n\n{prompt}\n"
        "Respond ONLY with a valid JSON object matching the requested structure. "
        "For code snippets, use 'code' (string) and 'explanation' (string or null). "
        "For task lists, use 'tasks' (array of objects with 'description' fields). "
        "Do not include any text, Markdown, or code blocks outside the JSON structure. "
        "Example for code: {'code': 'print(42)', 'explanation': 'Prints 42'} "
        "Example for tasks: {'tasks': [{'description': 'Task 1'}, {'description': 'Task 2'}]}"
    )
    response = client.messages.create(
        model=MODEL,
        messages=[{"role": "user", "content": full_prompt}],
        max_tokens=max_tokens
    )
    response_text = response.content[0].text.strip()  # type: ignore[attr-defined]
    # Fallback: Extract JSON if Claude adds extra text
    json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
    if json_match:
        response_json = json.loads(json_match.group(0))
    else:
        response_json = json.loads(response_text)
    return response_model(**response_json)

if __name__ == "__main__":
    system_prompt = "You are an AI assistant for DuckDB documentation."
    if os.getenv("ANTHROPIC_API_KEY"):
        try:
            response = generate_response("Generate a DuckDB query example with Python code", system_prompt)
            print(f"Code: {response.code}")
            print(f"Explanation: {response.explanation}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Skipping API test: ANTHROPIC_API_KEY missing in .env")