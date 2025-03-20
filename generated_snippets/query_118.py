# Generated: 2025-03-19 20:26:55.573993
# Result: [15, 25, 35, 45]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("""
SELECT array_transform([10, 20, 30, 40], x -> x + 5) as incremented_array
""").fetchone()[0]

print(result)  # Outputs: [15, 25, 35, 45]