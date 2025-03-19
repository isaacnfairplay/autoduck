# Generated: 2025-03-19 14:07:47.565939
# Result: [([1, 0, 2, 1],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate array_transform with modulo operation
result = conn.execute("""SELECT array_transform([10, 15, 20, 25], x -> x % 3) as transformed_array""").fetchall()

print(result[0][0])  # Outputs: [1, 0, 2, 1]