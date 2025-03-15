import duckdb
from typing import Optional, Literal, TypeAlias
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)
SNIPPET_DIR = "generated_snippets"
os.makedirs(SNIPPET_DIR, exist_ok=True)

SnippetResult: TypeAlias = tuple[bool, Optional[str]]
VarInfo: TypeAlias = dict[str, str]
Category: TypeAlias = Literal["connect", "query", "other"]

class SnippetBuilder:
    def __init__(self) -> None:
        self.context = {}
        self.conn: Optional[duckdb.DuckDBPyConnection] = None
        self.prev_vars = set()

    def execute_snippet(self, snippet: str) -> SnippetResult:
        """Execute a Python snippet and return its success status and result/error."""
        if not snippet.strip():
            return False, "Empty snippet"
        try:
            exec(snippet, self.context)
            if "conn" in self.context and not self.conn:
                self.conn = self.context["conn"]
            result = self.context.get("result")
            return True, str(result) if result else None
        except Exception as e:
            return False, str(e)

    def get_variable_info(self, snippet: str) -> VarInfo:
        """Get information about variables introduced by a snippet."""
        new_vars = {}
        current_vars = set(self.context.keys())
        added_vars = current_vars - self.prev_vars
        for var in added_vars:
            obj = self.context[var]
            var_type = type(obj).__name__
            details = f"Type: {var_type}"
            if isinstance(obj, duckdb.DuckDBPyRelation):
                details += "\nAttributes: .query(), .columns, .fetchall()"
            elif isinstance(obj, duckdb.DuckDBPyConnection):
                details += "\nAttributes: .execute(), .close()"
            new_vars[var] = details
        self.prev_vars = current_vars
        return new_vars

    def store_snippet(self, category: Category, snippet: str, result: Optional[str], valid: bool, vars_info: VarInfo) -> str:
        """Store a snippet with metadata in the snippets directory."""
        seq = len([f for f in os.listdir(SNIPPET_DIR) if f.startswith(category)])
        filename = f"{SNIPPET_DIR}/{category}_{seq:03d}.py"
        with open(filename, "w") as f:
            f.write(f"# Generated: {datetime.now()}\n# Result: {result}\n# Valid: {valid}\n")
            for var, info in vars_info.items():
                f.write(f"# Variable {var}: {info}\n")
            f.write(snippet)
        return filename

if __name__ == "__main__":
    builder = SnippetBuilder()
    snippet = "conn = duckdb.connect(':memory:')\nresult = conn.execute('SELECT 42').fetchall()"
    valid, result = builder.execute_snippet(snippet)
    print(f"Valid: {valid}, Result: {result}")
    vars_info = builder.get_variable_info(snippet)
    filename = builder.store_snippet("connect", snippet, result, valid, vars_info)
    print(f"Snippet stored at: {filename}")