import os
import anthropic
import re
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
MODEL = os.getenv("ANTHROPIC_MODEL", "claude-3-5-haiku-20241022")

def generate_response(prompt: str, system_prompt: str, max_tokens: int = 500) -> str:
    response = client.messages.create(
        model=MODEL,
        system=system_prompt,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    return response.content[0].text.strip()

def extract_code(response: str) -> str:
    match = re.search(r"```python(.*?)```", response, re.DOTALL)
    return match.group(1).strip() if match else response.strip()

if __name__ == "__main__":
    system_prompt = "You are an AI assistant for DuckDB documentation."
    if os.getenv("ANTHROPIC_API_KEY"):
        response = generate_response("Generate a concise DuckDB query example with Python code", system_prompt)
        print(f"Response: {response}")
        code = extract_code(response)
        print(f"Extracted Code: {code if code else 'No Python code found in response'}")
    else:
        print("Skipping API test: ANTHROPIC_API_KEY missing in .env")