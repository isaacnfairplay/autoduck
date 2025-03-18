# Generated: 2025-03-16 22:43:24.319761
# Result: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a recursive common table expression to generate a series
result = conn.execute('''
WITH RECURSIVE
    number_series(n) AS (
        SELECT 1
        UNION ALL
        SELECT n + 1 FROM number_series WHERE n < 10
    )
SELECT n, n * n AS squared
FROM number_series
''').fetchall()

# Print the generated series with squares
for row in result:
    print(f'Number: {row[0]}, Squared: {row[1]}')