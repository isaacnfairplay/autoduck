# Generated: 2025-03-19 16:48:45.146646
# Result: [([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create array column and transform values
result = conn.execute('''
    SELECT [1, 2, 3, 4, 5] AS original_array,
           array_transform([1, 2, 3, 4, 5], x -> x * x) AS squared_array
''').fetchall()

print(result)