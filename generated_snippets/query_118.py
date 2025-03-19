# Generated: 2025-03-19 13:20:14.615954
# Result: [1, 4, 9, 16, 25]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate array_transform for squaring list elements
result = conn.execute(
    "SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) AS squared_list"
).fetchone()[0]

print(result)  # Output: [1, 4, 9, 16, 25]