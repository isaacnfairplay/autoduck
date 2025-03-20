# Generated: 2025-03-19 21:27:52.908690
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample list of integers
conn.sql('CREATE TABLE numbers AS SELECT [1, 2, 3, 4, 5] AS num_list')

# Use array_transform to square each element
result = conn.sql('''
    SELECT array_transform(num_list, x -> x * x) AS squared_list
    FROM numbers
''').fetchall()

print(result)  # Should output: [[1, 4, 9, 16, 25]]