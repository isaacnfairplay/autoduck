# Generated: 2025-03-19 13:19:19.276551
# Result: [1, 4, 9, 16, 25]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a list and transform it using array_transform
result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) as squared_list
""").fetchone()[0]

print(result)  # Will output [1, 4, 9, 16, 25]