import time
import json
from typing import List, Tuple
import os
from dotenv import load_dotenv

class TokenTracker:
    def __init__(self, c_in: float = 15e-6, c_out: float = 3e-6, history_file: str = "token_usage.json"):
        self.c_in = c_in  # Cost per input token ($15/MT for Claude 3.7 Sonnet)
        self.c_out = c_out  # Cost per output token ($3/MT for Claude 3.7 Sonnet)
        self.history_file = history_file
        self.usage_history: List[Tuple[float, int, int]] = []  # (timestamp, input_tokens, output_tokens)
        self.reload_limits()  # Initial load of limits
        self.load_history()

    def reload_limits(self):
        """Reload token limits from .env file."""
        load_dotenv(override=True)  # Reload .env, overriding existing values
        self.hourly_input_limit = int(os.getenv("HOURLY_INPUT_TOKEN_LIMIT", 10000))  # Default: 10,000 input tokens
        self.hourly_output_limit = int(os.getenv("HOURLY_OUTPUT_TOKEN_LIMIT", 2000))  # Default: 2,000 output tokens
        print(f"Reloaded token limits: Input={self.hourly_input_limit}, Output={self.hourly_output_limit}")

    def load_history(self):
        try:
            with open(self.history_file, "r") as f:
                data = json.load(f)
                self.usage_history = [(float(t), int(i), int(o)) for t, i, o in data]
        except FileNotFoundError:
            self.usage_history = []

    def save_history(self):
        with open(self.history_file, "w") as f:
            json.dump(self.usage_history, f)

    def add_usage(self, input_tokens: int, output_tokens: int):
        timestamp = time.time()
        self.usage_history.append((timestamp, input_tokens, output_tokens))
        self.save_history()

    def get_current_usage(self) -> tuple[int, int]:
        current_time = time.time()
        total_input = 0
        total_output = 0
        # Sum usage within the last hour
        self.usage_history = [entry for entry in self.usage_history if current_time - entry[0] < 3600]
        for t, i, o in self.usage_history:
            total_input += i
            total_output += o
        return total_input, total_output

    def get_current_cost(self) -> float:
        input_tokens, output_tokens = self.get_current_usage()
        return input_tokens * self.c_in + output_tokens * self.c_out

    def can_make_call(self, estimated_input_tokens: int, estimated_output_tokens: int = 500) -> bool:
        current_input, current_output = self.get_current_usage()
        input_ok = current_input + estimated_input_tokens < self.hourly_input_limit
        output_ok = current_output + estimated_output_tokens < self.hourly_output_limit
        if not( input_ok and output_ok):
            print(f"Current Input {current_input} and Current Output {current_output}")
        return input_ok and output_ok

    def wait_until_reset(self) -> float:
        current_time = time.time()
        if not self.usage_history:
            return 0
        for t, _, _ in self.usage_history:
            if current_time - t >= 3600:
                return 0  # Some usage has expired, recheck limits
        # Wait until the oldest entry expires (within 1 hour)
        wait_time = 3600 - (current_time - self.usage_history[0][0])
        return min(wait_time, 3600)  # Cap wait time at 1 hour