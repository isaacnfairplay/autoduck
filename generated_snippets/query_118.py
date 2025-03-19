# Generated: 2025-03-19 18:43:36.189206
# Result: [10, 20, 30, 40]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Define array and apply transformation
result = conn.execute('SELECT array_transform([5, 10, 15, 20], x -> x * 2) as doubled_array').fetchone()[0]

print(result)