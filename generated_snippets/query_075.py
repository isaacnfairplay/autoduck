# Generated: 2025-03-16 22:50:34.598960
# Result: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a recursive common table expression (CTE) to generate a series
result = con.execute('''
WITH RECURSIVE number_series(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM number_series WHERE n < 10
)
SELECT * FROM number_series
''').fetchall()

print(result)