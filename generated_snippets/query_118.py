# Generated: 2025-03-19 16:28:34.707289
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create list array and square each element
result = conn.execute("""
WITH nums(values) AS (VALUES ([1,2,3,4,5]))
SELECT array_transform(values, x -> x * x) as squared_values FROM nums
""").fetchall()

print(result)