# Generated: 2025-03-19 18:14:30.881698
# Result: ([11, 12, 13, 14],)
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array").fetchone()
print(result[0])