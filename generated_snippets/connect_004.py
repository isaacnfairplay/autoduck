# Generated: 2025-03-15 16:20:57.853073
# Result: [(42,)]
# Valid: True
# Variable __builtins__: Type: dict
# Variable conn: Type: DuckDBPyConnection
Attributes: .execute(), .close()
# Variable duckdb: Type: module
# Variable result: Type: list
import duckdb
conn = duckdb.connect(':memory:')
result = conn.execute('SELECT 42').fetchall()