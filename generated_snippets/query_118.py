# Generated: 2025-03-19 21:45:18.151140
# Result: [([11, 12, 13, 14],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("""SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array""").fetchall()

print(result[0][0])