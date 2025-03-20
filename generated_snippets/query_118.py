# Generated: 2025-03-19 20:14:54.625634
# Result: [15, 25, 35]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("SELECT array_transform([10, 20, 30], x -> x + 5) as incremented_array").fetchone()[0]
print(result)