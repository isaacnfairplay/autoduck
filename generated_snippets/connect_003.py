# Generated: 2025-03-15 16:09:10.142101
# Result: [(42,)]
# Valid: True
# Variable result: Type: list
# Variable conn: Type: DuckDBPyConnection
Attributes: .execute(), .close()
# Variable duckdb: Type: module
# Variable __builtins__: Type: dict
import duckdb
conn = duckdb.connect(':memory:')
result = conn.execute('SELECT 42').fetchall()