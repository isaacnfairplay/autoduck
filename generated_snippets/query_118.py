# Generated: 2025-03-19 14:29:32.363191
# Result: [1, 4, 9, 16, 25]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and transform an array of numbers using array_transform
result = conn.execute('''
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) AS squared_values
''').fetchone()[0]

print(result)  # Outputs: [1, 4, 9, 16, 25]