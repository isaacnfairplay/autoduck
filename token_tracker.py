import time
import json
from typing import List, Tuple

class TokenTracker:
    def __init__(self, c_in: float = 3e-6, c_out: float = 15e-6, daily_limit: float = 1.0, history_file: str = "token_usage.json"):
        self.c_in = c_in  # Cost per input token ($0.000003 for Claude 3.5 Sonnet)
        self.c_out = c_out  # Cost per output token ($0.000015 for Claude 3.5 Sonnet)
        self.daily_limit = daily_limit  # Daily cost limit in dollars
        self.history_file = history_file
        self.usage_history: List[Tuple[float, int, int]] = []  # (timestamp, input_tokens, output_tokens)
        self.load_history()

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

    def get_current_cost(self):
        current_time = time.time()
        total_cost = 0.0
        # Sum costs for usage within the last 24 hours
        self.usage_history = [entry for entry in self.usage_history if current_time - entry[0] < 86400]
        for t, i, o in self.usage_history:
            total_cost += i * self.c_in + o * self.c_out
        return total_cost

    def can_make_call(self, estimated_input_tokens: int, estimated_output_tokens: int = 500):
        estimated_cost = estimated_input_tokens * self.c_in + estimated_output_tokens * self.c_out
        current_cost = self.get_current_cost()
        return current_cost + estimated_cost < self.daily_limit

    def wait_until_reset(self):
        current_time = time.time()
        if not self.usage_history:
            return 0
        for t, _, _ in self.usage_history:
            if current_time - t >= 86400:
                return 0  # Some usage has expired, recheck cost
        # Wait until the oldest entry expires
        return 86400 - (current_time - self.usage_history[0][0])