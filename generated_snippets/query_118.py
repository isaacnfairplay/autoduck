# Generated: 2025-03-19 09:37:22.717800
# Result: [(1, 'John'), (2, 'Jane'), (3, 'Bob')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.sql("SELECT * FROM (VALUES (1, 'John'), (2, 'Jane'), (3, 'Bob')) t(id, name)").fetchall()
print(result)