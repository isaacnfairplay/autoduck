# Generated: 2025-03-19 18:45:21.448858
# Result: [2, 4, 6, 8]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create an array and transform it using array_transform
result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4], x -> x * 2) as doubled_array
""").fetchone()[0]

print(result)  # Should output [2, 4, 6, 8]