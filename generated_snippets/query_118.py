# Generated: 2025-03-19 13:53:45.996166
# Result: [([3, 5, 7, 9],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute('SELECT array_transform([1, 2, 3, 4], x -> x * 2 + 1) as transformed_array').fetchall()
print(result)