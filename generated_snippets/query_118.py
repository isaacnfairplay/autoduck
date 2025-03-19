# Generated: 2025-03-19 09:20:15.620989
# Result: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a recursive common table expression (CTE) for generating a number series
result = conn.execute('''
WITH RECURSIVE number_series(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM number_series WHERE n < 10
)
SELECT n, n * n as squared FROM number_series
''').fetchall()

for row in result:
    print(f'Number: {row[0]}, Squared: {row[1]}')