# Generated: 2025-03-19 15:40:50.571608
# Result: [4, 9, 16, 25]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("SELECT array_transform([2, 3, 4, 5], x -> x * x) as squared_array").fetchone()[0]
print(result)