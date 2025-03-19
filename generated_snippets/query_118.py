# Generated: 2025-03-19 17:10:02.647212
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate array element transformation via functional SQL
result = conn.sql('''
WITH nums(arr) AS (VALUES ([1, 2, 3, 4, 5]))
SELECT array_transform(arr, x -> x * x) AS squared_nums
FROM nums
''').fetchall()

print(result)