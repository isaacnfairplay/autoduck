# Generated: 2025-03-19 17:34:16.653567
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with lists of integers
conn.sql("""
CREATE TABLE numbers AS
SELECT [1, 2, 3, 4, 5] AS number_list
""")

# Use array_transform to square each element in the list
result = conn.sql("""
SELECT array_transform(number_list, x -> x * x) AS squared_list
FROM numbers
""").fetchall()

print(result)  # Expected output: [1, 4, 9, 16, 25]