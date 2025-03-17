import os
import anthropic
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Union, Type
import json
import re
from anthropic.types import TextBlock, Message
import time

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
MODEL = os.getenv("ANTHROPIC_MODEL", "claude-3-5-haiku-20241022")

class CodeSnippet(BaseModel):
    code: str = Field(description="The Python code snippet")
    explanation: str | None = Field(default=None, description="Explanation of the code")

class Task(BaseModel):
    description: str = Field(description="Description of the task")

class TaskList(BaseModel):
    tasks: list[Task] = Field(description="List of suggested tasks")

def generate_response(prompt: str, system_prompt: str, max_tokens: int = 500, response_model: Type[Union[CodeSnippet, TaskList]] = CodeSnippet, retries: int = 3) -> Union[CodeSnippet, TaskList]:
    """Generate a structured JSON response with retries for malformed output."""
    full_prompt = (
        f"{system_prompt}\n\n{prompt}\n"
        "Respond **ONLY** with a complete, valid JSON object matching the requested structure. "
        "For code snippets, include 'code' (string) and 'explanation' (string or null). "
        "For task lists, include 'tasks' (array of objects with 'description' fields). "
        "Ensure all strings are properly terminated and the JSON has no syntax errors. "
        "Do not include extra text, Markdown, or code blocks outside the JSON. "
        "Example for code: {'code': 'print(42)', 'explanation': 'Prints 42'} "
        "Example for tasks: {'tasks': [{'description': 'Task 1'}, {'description': 'Task 2'}]}"
    )
    for attempt in range(retries):
        try:
            response: Message = client.messages.create(
                model=MODEL,
                messages=[{"role": "user", "content": full_prompt}],
                max_tokens=max_tokens
            )
            if not response.content or not isinstance(response.content[0], TextBlock):
                raise ValueError("Unexpected response content format")
            response_text = response.content[0].text.strip()
            # Fallback: Extract JSON if extra text is present
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                response_json_str = json_match.group(0)
            else:
                response_json_str = response_text
            response_json = json.loads(response_json_str)
            return response_model(**response_json)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Attempt {attempt + 1} failed: {e}. Response text: {response_text}")
            if attempt < retries - 1:
                time.sleep(2)  # Wait before retrying
            else:
                raise ValueError("Failed to get valid JSON after retries") from e  # type: ignore[return]

if __name__ == "__main__":
    system_prompt = "You are an AI assistant for DuckDB documentation."
    if os.getenv("ANTHROPIC_API_KEY"):
        try:
            response = generate_response("Generate a DuckDB query example with Python code", system_prompt)
            if isinstance(response, CodeSnippet):
                print(f"Code: {response.code}")
                print(f"Explanation: {response.explanation}")
            else:
                print("Received TaskList instead of CodeSnippet")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Skipping API test: ANTHROPIC_API_KEY missing in .env")