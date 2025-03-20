# Generated: 2025-03-19 21:12:11.813807
# Result: [11, 12, 13, 14]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.sql("SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array").fetchone()[0]
print(result)