# Generated: 2025-03-19 13:23:42.745070
# Result: [1, 4, 9, 16, 25]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Transform numeric array by squaring values
result = conn.execute(
    'SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) AS squared_list'
).fetchone()[0]

print(result)  # Output: [1, 4, 9, 16, 25]