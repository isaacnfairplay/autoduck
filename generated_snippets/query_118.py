# Generated: 2025-03-19 13:32:56.996380
# Result: [1, 4, 9, 16, 25]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Use array_transform to square each element of a numeric list
result = conn.execute('''
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) AS squared_array
''').fetchone()[0]

print(result)  # Outputs: [1, 4, 9, 16, 25]