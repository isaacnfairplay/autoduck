from typing import Type, Union
import json
import re
import time
from pydantic import BaseModel
from anthropic import Anthropic, Message
from anthropic.types.message import TextBlock
from token_tracker import TokenTracker

client = Anthropic()
MODEL = "claude-3-5-sonnet-20241022"  # Adjust as needed

token_tracker = TokenTracker(c_in=3e-6, c_out=15e-6, daily_limit=1.0)

class CodeSnippet(BaseModel):
    code: str
    explanation: str | None = None

class Task(BaseModel):
    description: str

class TaskList(BaseModel):
    tasks: list[Task]

class StringResponse(BaseModel):
    response: str

def generate_response(prompt: str, system_prompt: str, max_tokens: int = 500, response_model: Type[Union[CodeSnippet, TaskList, StringResponse]] = CodeSnippet, retries: int = 3) -> Union[CodeSnippet, TaskList, StringResponse]:
    # Determine prompt suffix based on response model
    if response_model == CodeSnippet:
        prompt_suffix = "Respond **ONLY** with a concise, valid JSON object containing 'code' (string) and 'explanation' (string or null). Ensure strings are terminated and JSON is complete. No extra text or Markdown outside JSON."
    elif response_model == TaskList:
        prompt_suffix = "Respond **ONLY** with a valid JSON object containing 'tasks' (array of objects with 'description' fields). Ensure JSON is complete. No extra text or Markdown outside JSON."
    else:  # StringResponse
        prompt_suffix = "Respond **ONLY** with a valid JSON object containing 'response' (string with your answer). If updating the system prompt, start with 'UPDATE PROMPT:' followed by the new instruction. Ensure JSON is complete."
    
    full_prompt = f"{system_prompt}\n\n{prompt}\n{prompt_suffix}"
    estimated_input_tokens = len(full_prompt.split())  # Rough estimate: ~1 token per word
    estimated_output_tokens = max_tokens  # Conservative estimate
    
    # Check if we can make the call
    if not token_tracker.can_make_call(estimated_input_tokens, estimated_output_tokens):
        wait_time = token_tracker.wait_until_reset()
        print(f"Token limit reached. Waiting {wait_time} seconds.")
        time.sleep(wait_time)
    
    for attempt in range(retries):
        try:
            response: Message = client.messages.create(
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
            if json_match:
                response_json_str = json_match.group(0)
            else:
                response_json_str = response_text
            response_json = json.loads(response_json_str)
            return response_model(**response_json)
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(2)
            else:
                # Fallback responses
                if response_model == CodeSnippet:
                    return CodeSnippet(code="print('Error: Failed to generate response')", explanation="Fallback due to repeated failures")
                elif response_model == TaskList:
                    return TaskList(tasks=[Task(description="Error: Failed to generate tasks")])
                else:
                    return StringResponse(response="Error: Failed to generate response")