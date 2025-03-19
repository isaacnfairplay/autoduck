# Generated: 2025-03-19 17:12:44.269581
# Result: [2, 4, 6, 8, 10]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create an array and transform its elements
result = conn.sql("""
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * 2) AS doubled_array
""").fetchone()[0]

print(result)  # Expected output: [2, 4, 6, 8, 10]