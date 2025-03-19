# Generated: 2025-03-19 18:17:53.016988
# Result: ([10, 20, 30, 40],)
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("SELECT array_transform([5, 10, 15, 20], x -> x * 2) as doubled_array").fetchone()
print(result[0])