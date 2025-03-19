# Generated: 2025-03-19 18:09:11.325062
# Result: [([1, 4, 9],), ([16, 25, 36],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample data with arrays
conn.sql("""
CREATE TABLE number_arrays AS
SELECT [1, 2, 3] AS original_array
UNION ALL
SELECT [4, 5, 6]
""")

# Use array_transform to square each array element
result = conn.sql("""
SELECT array_transform(original_array, x -> x * x) AS squared_array
FROM number_arrays
""").fetchall()

print(result)