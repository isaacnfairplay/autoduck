# Generated: 2025-03-19 16:57:17.929328
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with numeric lists
conn.sql('''
CREATE TABLE numbers_list AS
SELECT [1, 2, 3, 4, 5] AS nums
''')

# Transform list elements by squaring each value
result = conn.sql('''
SELECT array_transform(nums, x -> x * x) AS squared_nums
FROM numbers_list
''').fetchall()

print(result)  # Output: [1, 4, 9, 16, 25]