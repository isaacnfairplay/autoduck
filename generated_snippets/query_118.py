# Generated: 2025-03-19 18:12:48.684866
# Result: ([1, 2, 3, 4, 5], [11, 12, 13, 14, 15])
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create array and transform elements
result = conn.execute("""
    SELECT [1, 2, 3, 4, 5] as original_array,
           array_transform([1, 2, 3, 4, 5], x -> x + 10) as transformed_array
""").fetchone()

print(f"Original Array: {result[0]}")
print(f"Transformed Array: {result[1]}")