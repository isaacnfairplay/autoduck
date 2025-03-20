# Generated: 2025-03-19 21:16:29.106927
# Result: [10, 20, 30, 40]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.sql("SELECT array_transform([5, 10, 15, 20], x -> x * 2) as multiplied_array").fetchone()[0]
print(result)