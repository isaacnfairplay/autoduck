# Generated: 2025-03-19 14:01:46.845013
# Result: [([1, 0, 2, 1],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create array and transform with modulo
result = conn.execute("""
    SELECT array_transform([10, 15, 20, 25], x -> x % 3) as transformed_array
""").fetchall()

print(result[0][0])  # Should output [1, 0, 2, 1]