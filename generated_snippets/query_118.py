# Generated: 2025-03-19 15:55:12.135387
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Square numeric array values using array_transform
result = conn.execute('''
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) as squared_numbers
''').fetchall()

print(result[0][0])  # Outputs: [1, 4, 9, 16, 25]