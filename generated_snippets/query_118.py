# Generated: 2025-03-19 14:19:56.177541
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create an array and transform each element
result = conn.execute('''
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) AS squared_array
''').fetchall()

print(result[0][0])  # Output: [1, 4, 9, 16, 25]