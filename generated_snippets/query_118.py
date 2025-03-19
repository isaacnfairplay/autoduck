# Generated: 2025-03-19 19:14:24.099180
# Result: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with numeric arrays
conn.sql("""
CREATE TABLE numeric_arrays (nums INTEGER[]);

INSERT INTO numeric_arrays VALUES
([1, 2, 3]), 
([4, 5, 6]), 
([7, 8, 9]);

SELECT nums, array_transform(nums, x -> x + 10) AS transformed_nums
FROM numeric_arrays;
""").show()