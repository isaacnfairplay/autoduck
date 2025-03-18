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

def _get_prompt_suffix(response_model: Type[Union[CodeSnippet, TaskList, StringResponse]]) -> str:
    """Return the appropriate prompt suffix based on response model."""
    if response_model == CodeSnippet:
        return "Respond **ONLY** with a concise, valid JSON object containing 'code' (string) and 'explanation' (string or null). Ensure strings are terminated and JSON is complete. No extra text or Markdown outside JSON."
    elif response_model == TaskList:
        return "Respond **ONLY** with a valid JSON object containing 'tasks' (array of objects with 'description' fields). Ensure JSON is complete. No extra text or Markdown outside JSON."
    return "Respond **ONLY** with a valid JSON object containing 'response' (string). If updating the system prompt, start with 'UPDATE PROMPT:' followed by the new instruction. Ensure JSON is complete."

def _parse_response(response_text: str, response_model: Type[Union[CodeSnippet, TaskList, StringResponse]]) -> Union[CodeSnippet, TaskList, StringResponse]:
    """Parse and validate the response text into the specified model."""
    json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
    response_json_str = json_match.group(0) if json_match else response_text
    response_json = json.loads(response_json_str)
    return response_model(**response_json)

def _try_local_model(full_prompt: str, system_prompt: str, max_tokens: int, response_model: Type, retries: int) -> Tuple[Union[CodeSnippet, TaskList, StringResponse], str, bool]:
    """Attempt to generate a response using the local model with retries."""
    for attempt in range(retries):
        try:
            response = openai_client.chat.completions.create(
                model="local-model",
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
            result = _parse_response(response_text, response_model)
            return result, "Local Model", True
        except Exception as e:
            print(f"Local attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(2)
    return None, None, False

def _try_anthropic_model(full_prompt: str, token_tracker: TokenTracker, max_tokens: int, response_model: Type, retries: int, estimated_input_tokens: int) -> Tuple[Union[CodeSnippet, TaskList, StringResponse], str, bool]:
    """Attempt to generate a response using the Anthropic model with retries."""
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
            if not response.content or not isinstance(response.content[0], TextBlock):
                raise ValueError("Unexpected response content format")
            result = _parse_response(response_text, response_model)
            return result, "Anthropic", True
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Anthropic attempt {attempt + 1} failed: {e}. Response text: {response_text}")
            if attempt < retries - 1:
                time.sleep(2)
    return None, None, False

def generate_response(prompt: str, system_prompt: str, token_tracker: TokenTracker, max_tokens: int = 500, response_model: Type[Union[CodeSnippet, TaskList, StringResponse]] = CodeSnippet, retries: int = 3, use_remote: bool = False) -> Tuple[Union[CodeSnippet, TaskList, StringResponse], str]:
    """Generate a structured JSON response with simplified control flow."""
    prompt_suffix = _get_prompt_suffix(response_model)
    full_prompt = f"{system_prompt}\n\n{prompt}\n{prompt_suffix}"
    estimated_input_tokens = len(full_prompt.split())  # Rough estimate

    # Try local model first if enabled and not forced remote
    if USE_LOCAL_MODEL and not use_remote:
        print("Attempting local model via LMStudio...")
        result, model_used, success = _try_local_model(full_prompt, system_prompt, max_tokens, response_model, retries)
        if success:
            token_tracker.add_usage(estimated_input_tokens, max_tokens)  # Log usage for stats
            return result, model_used
        print("Local model failed after retries, switching to Anthropic")

    # Fallback to Anthropic
    print("Using Anthropic remote model...")
    result, model_used, success = _try_anthropic_model(full_prompt, token_tracker, max_tokens, response_model, retries, estimated_input_tokens)
    if success:
        return result, model_used

    # Fallback if all attempts fail
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