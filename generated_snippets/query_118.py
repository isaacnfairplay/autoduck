# Generated: 2025-03-19 20:52:06.069794
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with list column
conn.sql("""
CREATE TABLE numbers AS
SELECT [1, 2, 3, 4, 5] AS values
""")

# Transform list by squaring each element
result = conn.sql("""
SELECT array_transform(values, x -> x * x) AS squared_values
FROM numbers
""").fetchall()

print(result)  # Should output: [[1, 4, 9, 16, 25]]