# Generated: 2025-03-19 13:15:54.627675
# Result: [(1, 'Alice', 'Alice'), (2, 'Bob', 'Alice -> Bob'), (3, 'Charlie', 'Alice -> Charlie'), (4, 'David', 'Alice -> Bob -> David'), (5, 'Eve', 'Alice -> Charlie -> Eve')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE nums(x INTEGER)')
conn.execute('INSERT INTO nums VALUES (1), (2), (3), (4), (5)')
rel = conn.sql('SELECT x, x*x as squared FROM nums')
print(rel.execute().fetchall())