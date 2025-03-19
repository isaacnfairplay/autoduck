# Generated: 2025-03-19 17:33:23.386728
# Result: [1, 4, 9, 16, 25]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) AS squared_array").fetchone()[0]
print(result)