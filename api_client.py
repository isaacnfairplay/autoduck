import os
import anthropic
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Union, Type, Tuple
import json
import re
import time
from anthropic.types import TextBlock
from token_tracker import TokenTracker

load_dotenv()

# Anthropic client for remote model
anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
# OpenAI client for LMStudio local model
openai_client = OpenAI(base_url="http://localhost:6965/v1", api_key="not-needed")

# Configurable models from .env
REMOTE_MODEL = os.getenv("REMOTE_MODEL", "claude-3-5-sonnet")  # Default to Claude 3.5 Sonnet
USE_LOCAL_MODEL = os.getenv("USE_LOCAL_MODEL", "true").lower() == "true"  # Enable local model by default

class CodeSnippet(BaseModel):
    code: str = Field(description="The Python code snippet")
    explanation: str | None = Field(default=None, description="Explanation of the code")

class Task(BaseModel):
    description: str = Field(description="Description of the task")

class TaskList(BaseModel):
    tasks: list[Task] = Field(description="List of suggested tasks")

class StringResponse(BaseModel):
    response: str = Field(description="A string response, e.g., for Mega prompt feedback")

def generate_response(prompt: str, system_prompt: str, token_tracker: TokenTracker, max_tokens: int = 500, response_model: Type[Union[CodeSnippet, TaskList, StringResponse]] = CodeSnippet, retries: int = 3) -> Tuple[Union[CodeSnippet, TaskList, StringResponse], str]:
    """Generate a structured JSON response, trying local model first, then falling back to Anthropic. Returns (response, model_used)."""
    if response_model == CodeSnippet:
        prompt_suffix = "Respond **ONLY** with a concise, valid JSON object containing 'code' (string) and 'explanation' (string or null). Ensure strings are terminated and JSON is complete. No extra text or Markdown outside JSON."
    elif response_model == TaskList:
        prompt_suffix = "Respond **ONLY** with a valid JSON object containing 'tasks' (array of objects with 'description' fields). Ensure JSON is complete. No extra text or Markdown outside JSON."
    else:  # StringResponse
        prompt_suffix = "Respond **ONLY** with a valid JSON object containing 'response' (string). If updating the system prompt, start with 'UPDATE PROMPT:' followed by the new instruction. Ensure JSON is complete."

    full_prompt = f"{system_prompt}\n\n{prompt}\n{prompt_suffix}"
    estimated_input_tokens = len(full_prompt.split())  # Rough estimate: ~1 token per word

    # Test local model first if enabled
    if USE_LOCAL_MODEL:
        print("Attempting local model via LMStudio...")
        test_prompt = "Generate a simple Python print statement in JSON format: {'code': 'print(...)', 'explanation': '...'}"
        local_success = False
        for attempt in range(5):  # 5 attempts for local model
            try:
                response = openai_client.chat.completions.create(
                    model="local-model",  # Dummy value; LMStudio uses loaded model
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": test_prompt}
                    ],
                    max_tokens=100
                )
                response_text = response.choices[0].message.content.strip()
                json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                response_json_str = json_match.group(0) if json_match else response_text
                response_json = json.loads(response_json_str)
                if 'code' in response_json and isinstance(response_json['code'], str):
                    local_success = True
                    print(f"Local model succeeded after {attempt + 1} attempts")
                    break
            except Exception as e:
                print(f"Local test attempt {attempt + 1} failed: {e}")
                if attempt < 4:
                    time.sleep(1)
        
        if local_success:
            # Use local model for the actual request
            for attempt in range(retries):
                try:
                    response = openai_client.chat.completions.create(
                        model="local-model",  # Dummy value
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": full_prompt}
                        ],
                        max_tokens=max_tokens
                    )
                    input_tokens = response.usage.prompt_tokens
                    output_tokens = response.usage.completion_tokens
                    print(f"Local API call used {input_tokens} input tokens, {output_tokens} output tokens (no cost tracked)")
                    response_text = response.choices[0].message.content.strip()
                    json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                    response_json_str = json_match.group(0) if json_match else response_text
                    response_json = json.loads(response_json_str)
                    return response_model(**response_json), "Local Model"
                except Exception as e:
                    print(f"Local attempt {attempt + 1} failed: {e}")
                    if attempt < retries - 1:
                        time.sleep(2)
            print("Local model failed after retries, switching to Anthropic")

    # Fallback to Anthropic if local fails or disabled
    print("Using Anthropic remote model...")
    if not token_tracker.can_make_call(estimated_input_tokens, max_tokens):
        wait_time = token_tracker.wait_until_reset()
        print(f"Hourly token limit reached (Input: {token_tracker.hourly_input_limit}, Output: {token_tracker.hourly_output_limit}). Waiting {wait_time:.2f} seconds.")
        time.sleep(wait_time)

    for attempt in range(retries):
        try:
            response = anthropic_client.messages.create(
                model=REMOTE_MODEL,
                messages=[{"role": "user", "content": full_prompt}],
                max_tokens=max_tokens
            )
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            token_tracker.add_usage(input_tokens, output_tokens)
            print(f"Anthropic API call used {input_tokens} input tokens, {output_tokens} output tokens. Current hourly cost: ${token_tracker.get_current_cost():.4f}")
            response_text = response.content[0].text.strip()
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            response_json_str = json_match.group(0) if json_match else response_text
            response_json = json.loads(response_json_str)
            return response_model(**response_json), "Anthropic"
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Anthropic attempt {attempt + 1} failed: {e}. Response text: {response_text}")
            if attempt < retries - 1:
                time.sleep(2)
    
    # Fallback return if all retries fail
    if response_model == CodeSnippet:
        return CodeSnippet(code="print('Error: Failed to generate response')", explanation="Fallback due to repeated failures"), "Fallback"
    elif response_model == TaskList:
        return TaskList(tasks=[Task(description="Error: Failed to generate tasks")]), "Fallback"
    else:
        return StringResponse(response="Error: Failed to generate response"), "Fallback"

if __name__ == "__main__":
    system_prompt = "You are an AI assistant for DuckDB documentation."
    token_tracker = TokenTracker()
    if os.getenv("ANTHROPIC_API_KEY"):
        try:
            response, model_used = generate_response("Generate a DuckDB query example with Python code", system_prompt, token_tracker)
            if isinstance(response, CodeSnippet):
                print(f"Generated by: {model_used}")
                print(f"Code: {response.code}")
                print(f"Explanation: {response.explanation}")
            else:
                print("Unexpected response type")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Skipping API test: ANTHROPIC_API_KEY missing in .env")