# Generated: 2025-03-19 13:12:35.619647
# Result: [([2, 4, 6, 8],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute('SELECT array_transform([1, 2, 3, 4], x -> x * 2) as doubled_array').fetchall()
print(result)