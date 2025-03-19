# Generated: 2025-03-19 19:08:24.866739
# Result: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with array column
conn.sql("""
CREATE TABLE numbers (nums INTEGER[]);

INSERT INTO numbers VALUES
([1, 2, 3]), 
([4, 5, 6]), 
([7, 8, 9]);

SELECT nums, array_transform(nums, x -> x * 2) AS doubled_nums
FROM numbers;
""").show()