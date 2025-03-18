import duckdb
from typing import Optional, Literal, TypeAlias, Dict, Any, Set
import os
import logging
import inspect
from datetime import datetime
import chardet  # For detecting file encoding

logger = logging.getLogger(__name__)
SNIPPET_DIR = "generated_snippets"
os.makedirs(SNIPPET_DIR, exist_ok=True)

SnippetResult: TypeAlias = tuple[bool, Optional[str]]
VarInfo: TypeAlias = Dict[str, str]
Category: TypeAlias = Literal["connect", "query", "other"]

class SnippetBuilder:
    def __init__(self) -> None:
        self.context: Dict[str, Any] = {}
        self.conn: Optional[duckdb.DuckDBPyConnection] = None
        self.prev_vars: Set[str] = set()
        self.convert_snippets_to_utf8()  # Convert existing snippets to UTF-8 at startup

    def convert_snippets_to_utf8(self) -> None:
        """Convert all files in generated_snippets to UTF-8, preserving original line endings."""
        for filename in os.listdir(SNIPPET_DIR):
            filepath = os.path.join(SNIPPET_DIR, filename)
            if not os.path.isfile(filepath):
                continue

            # Read the file in binary mode to preserve exact bytes
            with open(filepath, "rb") as f:
                raw_data = f.read()

            # Detect current encoding
            detected = chardet.detect(raw_data)
            current_encoding = detected["encoding"] or "utf-8"

            if current_encoding.lower() != "utf-8":
                try:
                    # Decode to string, preserving original content
                    content = raw_data.decode(current_encoding, errors="replace")
                    # Encode back to UTF-8 bytes without altering line endings
                    utf8_data = content.encode("utf-8")
                    # Write in binary mode to avoid newline normalization
                    with open(filepath, "wb") as f:
                        f.write(utf8_data)
                    logger.info(f"Converted {filename} from {current_encoding} to UTF-8")
                except Exception as e:
                    logger.error(f"Failed to convert {filename} to UTF-8: {e}")
            else:
                logger.debug(f"{filename} is already UTF-8")

    def execute_snippet(self, snippet: str) -> SnippetResult:
        if not snippet.strip():
            return False, "Empty snippet"
        try:
            exec(snippet, self.context)
            if "conn" in self.context and self.conn is None:
                self.conn = self.context["conn"]
            result = self.context.get("result")
            return True, str(result) if result is not None else None
        except Exception as e:
            return False, str(e)

    def get_variable_info(self, snippet: str) -> VarInfo:
        new_vars: VarInfo = {}
        current_vars = set(self.context.keys())
        added_vars = current_vars - self.prev_vars

        for var in added_vars:
            if var in ("duckdb", "__builtins__"):
                continue
            obj = self.context[var]
            var_type = type(obj).__name__
            details = f"Type: {var_type}"

            attributes = []
            for attr in dir(obj):
                if attr.startswith("__") or attr in dir(object):
                    continue
                try:
                    attr_value = getattr(obj, attr)
                    if inspect.ismethod(attr_value) or inspect.isfunction(attr_value):
                        attributes.append(f"{attr}()")
                    else:
                        attributes.append(attr)
                except Exception:
                    continue

            if attributes:
                details += "\n# Attributes/Methods: " + ", ".join(sorted(attributes))

            new_vars[var] = details

        self.prev_vars = current_vars
        return new_vars

    def store_snippet(self, category: Category, snippet: str, result: Optional[str], valid: bool, vars_info: VarInfo) -> str:
        seq = len([f for f in os.listdir(SNIPPET_DIR) if f.startswith(f"{category}_")])
        filename = f"{SNIPPET_DIR}/{category}_{seq:03d}.py"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Generated: {datetime.now()}\n# Result: {result}\n# Valid: {valid}\n")
            for var, info in vars_info.items():
                f.write(f"# Variable {var}: {info}\n")
            f.write(snippet)
        return filename

if __name__ == "__main__":
    # Configure basic logging for demonstration
    logging.basicConfig(level=logging.INFO)
    
    builder = SnippetBuilder()
    snippet = "import duckdb\nconn = duckdb.connect(':memory:')\nresult = conn.execute('SELECT 42').fetchall()"
    valid, result = builder.execute_snippet(snippet)
    print(f"Valid: {valid}, Result: {result}")
    vars_info = builder.get_variable_info(snippet)
    for var, info in vars_info.items():
        print(f"Variable {var}: {info}")
    filename = builder.store_snippet("connect", snippet, result, valid, vars_info)
    print(f"Snippet stored at: {filename}")