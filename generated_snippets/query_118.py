# Generated: 2025-03-19 13:42:23.216268
# Result: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
# Valid: True
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create and populate recursive CTE for generating number series
result = conn.execute('''
WITH RECURSIVE
  number_series(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM number_series WHERE n < 10
  )
SELECT * FROM number_series
''').fetchall()

print(result)