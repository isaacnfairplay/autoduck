# Generated: 2025-03-19 21:03:25.837600
# Result: [([11, 12, 13, 14, 15],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.sql('SELECT array_transform([1, 2, 3, 4, 5], x -> x + 10) as incremented_array').fetchall()
print(result)