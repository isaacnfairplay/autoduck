# Generated: 2025-03-19 15:17:42.748971
# Result: [1, 4, 9, 16, 25]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Transform numeric array by applying square operation
result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) AS squared_array
""").fetchone()[0]

print(result)  # Output: [1, 4, 9, 16, 25]