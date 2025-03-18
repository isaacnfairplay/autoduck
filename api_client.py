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
LOCAL_MAX_TOKENS = int(os.getenv("LOCAL_MAX_TOKENS", 1000))  # Default to 1000 for local model

class CodeSnippet(BaseModel):
    code: str = Field(description="The Python code snippet")
    explanation: str | None = Field(default=None, description="Explanation of the code")

class Task(BaseModel):
    description: str = Field(description="Description of the task")

class TaskList(BaseModel):
    tasks: list[Task] = Field(description="List of suggested tasks")

class StringResponse(BaseModel):
    response: str = Field(description="A string response, e.g., for Mega prompt feedback")

class ModelResponseError(Exception):
    """Custom exception for model response failures."""
    pass

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

def _try_local_model(full_prompt: str, system_prompt: str, max_tokens: int, response_model: Type, retries: int) -> Tuple[Union[CodeSnippet, TaskList, StringResponse], str]:
    """Attempt to generate a response using the local model with retries, feeding back errors."""
    prompt = full_prompt
    for attempt in range(retries):
        try:
            response = openai_client.chat.completions.create(
                model="local-model",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=LOCAL_MAX_TOKENS,
                timeout=7200  # 2 hours timeout
            )
            usage = response.usage
            input_tokens = usage.prompt_tokens if usage else 0
            output_tokens = usage.completion_tokens if usage else 0
            print(f"Local API call used {input_tokens} input tokens, {output_tokens} output tokens (no cost tracked)")
            response_text = response.choices[0].message.content
            if response_text is None:
                raise ValueError("Response content is None")
            response_text = response_text.strip()
            result = _parse_response(response_text, response_model)
            return result, "Local Model"
        except (json.JSONDecodeError, ValueError) as e:
            error_msg = f"Previous attempt failed: {str(e)}. Please correct the response format."
            print(f"Local attempt {attempt + 1} failed: {error_msg}")
            if attempt < retries - 1:
                prompt = f"{full_prompt}\n\n{error_msg}"
                time.sleep(2)
            else:
                raise ModelResponseError(f"Local model failed after {retries} attempts: {str(e)}")
        except Exception as e:
            print(f"Local attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(2)
            else:
                raise ModelResponseError(f"Local model failed after {retries} attempts: {str(e)}")

def _try_anthropic_model(full_prompt: str, token_tracker: TokenTracker, max_tokens: int, response_model: Type, retries: int, estimated_input_tokens: int) -> Tuple[Union[CodeSnippet, TaskList, StringResponse], str]:
    """Attempt to generate a response using the Anthropic model with retries and token limits."""
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
            if not response.content or not isinstance(response.content[0], TextBlock):
                raise ValueError("Unexpected response content format")
            response_text = response.content[0].text.strip()
            result = _parse_response(response_text, response_model)
            return result, "Anthropic"
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Anthropic attempt {attempt + 1} failed: {e}. Response text: {response.content if response.content else 'None'}")
            if attempt < retries - 1:
                time.sleep(2)
            else:
                raise ModelResponseError(f"Anthropic model failed after {retries} attempts: {str(e)}")
        except Exception as e:
            print(f"Anthropic attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(2)
            else:
                raise ModelResponseError(f"Anthropic model failed after {retries} attempts: {str(e)}")

def generate_response(prompt: str, system_prompt: str, token_tracker: TokenTracker, max_tokens: int = 500, response_model: Type[Union[CodeSnippet, TaskList, StringResponse]] = CodeSnippet, retries: int = 3, use_remote: bool = False) -> Tuple[Union[CodeSnippet, TaskList, StringResponse], str]:
    """Generate a structured JSON response with simplified control flow, no token limits for local model."""
    prompt_suffix = _get_prompt_suffix(response_model)
    full_prompt = f"{system_prompt}\n\n{prompt}\n{prompt_suffix}"
    estimated_input_tokens = len(full_prompt.split())  # Rough estimate

    # Try local model first if enabled and not forced remote, no token limit check
    if USE_LOCAL_MODEL and not use_remote:
        print("Attempting local model via LMStudio...")
        try:
            result, model_used = _try_local_model(full_prompt, system_prompt, max_tokens, response_model, retries)
            token_tracker.add_usage(estimated_input_tokens, LOCAL_MAX_TOKENS)  # Log usage for stats only
            return result, model_used
        except ModelResponseError as e:
            print(f"Local model exhausted retries: {e}")
            print("Switching to Anthropic")

    # Fallback to Anthropic with token limits
    print("Using Anthropic remote model...")
    try:
        result, model_used = _try_anthropic_model(full_prompt, token_tracker, max_tokens, response_model, retries, estimated_input_tokens)
        return result, model_used
    except ModelResponseError as e:
        print(f"Anthropic model exhausted retries: {e}")

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