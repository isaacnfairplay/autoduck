# Generated: 2025-03-19 13:39:01.076210
# Result: [([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])]
# Valid: True
# Variable values: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

conn = duckdb.connect(':memory:')

# Create array column and transform values
result = conn.execute('''
    SELECT [1, 2, 3, 4, 5] as original_array,
           array_transform([1, 2, 3, 4, 5], x -> x * x) as squared_array
''').fetchall()

print(result)