# Generated: 2025-03-19 21:39:05.248637
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create list with array_transform to square numbers
result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) as squared_nums
""").fetchall()

print(result[0][0])  # Output: [1, 4, 9, 16, 25]