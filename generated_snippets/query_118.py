# Generated: 2025-03-19 17:01:36.349476
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
# Variable numbers: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

conn = duckdb.connect(':memory:')

# Create integer array and transform elements
result = conn.sql('''
WITH nums(arr) AS (VALUES ([1, 2, 3, 4, 5]))
SELECT array_transform(arr, x -> x * x) AS squared_nums
FROM nums
''').fetchall()

print(result)