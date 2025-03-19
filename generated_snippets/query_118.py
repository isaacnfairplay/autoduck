# Generated: 2025-03-19 19:30:44.655126
# Result: [([3, 6, 9, 12, 15],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute('SELECT array_transform([1, 2, 3, 4, 5], x -> x * 3) as tripled_array').fetchall()
print(result[0][0])