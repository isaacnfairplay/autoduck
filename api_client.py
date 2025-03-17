import os
import anthropic
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Union, Type
import json
import re
import time
from anthropic.types import TextBlock
from token_tracker import TokenTracker

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
MODEL = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")

token_tracker = TokenTracker(c_in=3e-6, c_out=15e-6, daily_limit=1.0)

class CodeSnippet(BaseModel):
    code: str = Field(description="The Python code snippet")
    explanation: str | None = Field(default=None, description="Explanation of the code")

class Task(BaseModel):
    description: str = Field(description="Description of the task")

class TaskList(BaseModel):
    tasks: list[Task] = Field(description="List of suggested tasks")

class StringResponse(BaseModel):
    response: str = Field(description="A string response, e.g., for Mega prompt feedback")

def generate_response(prompt: str, system_prompt: str, max_tokens: int = 500, response_model: Type[Union[CodeSnippet, TaskList, StringResponse]] = CodeSnippet, retries: int = 3) -> Union[CodeSnippet, TaskList, StringResponse]:
    """Generate a structured JSON response with retries for malformed output."""
    if response_model == CodeSnippet:
        prompt_suffix = "Respond **ONLY** with a concise, valid JSON object containing 'code' (string) and 'explanation' (string or null). Ensure strings are terminated and JSON is complete. No extra text or Markdown outside JSON."
    elif response_model == TaskList:
        prompt_suffix = "Respond **ONLY** with a valid JSON object containing 'tasks' (array of objects with 'description' fields). Ensure JSON is complete. No extra text or Markdown outside JSON."
    else:  # StringResponse
        prompt_suffix = "Respond **ONLY** with a valid JSON object containing 'response' (string). If updating the system prompt, start with 'UPDATE PROMPT:' followed by the new instruction. Ensure JSON is complete."
    
    full_prompt = f"{system_prompt}\n\n{prompt}\n{prompt_suffix}"
    estimated_input_tokens = len(full_prompt.split())  # Rough estimate: ~1 token per word
    
    if not token_tracker.can_make_call(estimated_input_tokens, max_tokens):
        wait_time = token_tracker.wait_until_reset()
        print(f"Token limit reached. Waiting {wait_time:.2f} seconds.")
        time.sleep(wait_time)

    for attempt in range(retries):
        try:
            response = client.messages.create(
                model=MODEL,
                messages=[{"role": "user", "content": full_prompt}],
                max_tokens=max_tokens
            )
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            token_tracker.add_usage(input_tokens, output_tokens)
            
            if not response.content or not isinstance(response.content[0], TextBlock):
                raise ValueError("Unexpected response content format")
            response_text = response.content[0].text.strip()
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            response_json_str = json_match.group(0) if json_match else response_text
            response_json = json.loads(response_json_str)
            return response_model(**response_json)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Attempt {attempt + 1} failed: {e}. Response text: {response_text}")
            if attempt < retries - 1:
                time.sleep(2)
    
    # Fallback return if all retries fail
    if response_model == CodeSnippet:
        return CodeSnippet(code="print('Error: Failed to generate response')", explanation="Fallback due to repeated failures")
    elif response_model == TaskList:
        return TaskList(tasks=[Task(description="Error: Failed to generate tasks")])
    else:
        return StringResponse(response="Error: Failed to generate response")

if __name__ == "__main__":
    system_prompt = "You are an AI assistant for DuckDB documentation."
    if os.getenv("ANTHROPIC_API_KEY"):
        try:
            response = generate_response("Generate a DuckDB query example with Python code", system_prompt)
            if isinstance(response, CodeSnippet):
                print(f"Code: {response.code}")
                print(f"Explanation: {response.explanation}")
            else:
                print("Unexpected response type")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Skipping API test: ANTHROPIC_API_KEY missing in .env")