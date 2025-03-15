# Generated: 2025-03-15 16:05:39.405621
# Result: name 'duckdb' is not defined
# Valid: False
# Variable __builtins__: Type: dict
conn = duckdb.connect(':memory:')
result = conn.execute('SELECT 42').fetchall()