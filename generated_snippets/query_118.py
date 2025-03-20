# Generated: 2025-03-19 21:32:11.682170
# Result: [([11, 12, 13, 14, 15],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample list of integers
conn.sql('CREATE TABLE numbers AS SELECT [1, 2, 3, 4, 5] AS num_list')

# Use array_transform to add 10 to each element
result = conn.sql('''
    SELECT array_transform(num_list, x -> x + 10) AS transformed_list
    FROM numbers
''').fetchall()

print(result)  # Should output: [[11, 12, 13, 14, 15]]