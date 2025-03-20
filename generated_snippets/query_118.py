# Generated: 2025-03-19 20:56:30.676886
# Result: [([11, 12, 13, 14, 15],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with numeric list
conn.sql("""CREATE TABLE numbers AS SELECT [1, 2, 3, 4, 5] AS values""")

# Transform list by adding 10 to each element
result = conn.sql("""SELECT array_transform(values, x -> x + 10) AS transformed_values FROM numbers""").fetchall()

print(result)  # Should output: [[11, 12, 13, 14, 15]]