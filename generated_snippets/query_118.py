# Generated: 2025-03-19 14:53:33.108446
# Result: [1, 4, 9, 16, 25]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Transform array by squaring each element
result = conn.execute('''
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) AS squared_array
''').fetchone()[0]

print(result)  # Outputs: [1, 4, 9, 16, 25]