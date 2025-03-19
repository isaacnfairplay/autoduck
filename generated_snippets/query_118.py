# Generated: 2025-03-19 13:25:21.243618
# Result: [1, 4, 9, 16]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute('SELECT array_transform([1, 2, 3, 4], x -> x * x) as squared_array').fetchone()[0]
print(result)