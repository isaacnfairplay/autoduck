# Generated: 2025-03-19 13:40:42.211583
# Result: [([1, 4, 9, 16],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute('SELECT array_transform([1, 2, 3, 4], x -> x * x) as squared_array').fetchall()
print(result)