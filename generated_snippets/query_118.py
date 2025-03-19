# Generated: 2025-03-19 14:41:27.735342
# Result: [2, 4, 6, 8, 10]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Transform array by doubling each numeric value
result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * 2) AS doubled_array
""").fetchone()[0]

print(result)  # Expected: [2, 4, 6, 8, 10]