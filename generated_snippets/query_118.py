# Generated: 2025-03-19 17:09:12.822325
# Result: [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a recursive common table expression (CTE) to generate Fibonacci sequence
result = conn.sql('''
WITH RECURSIVE fibonacci(n, a, b) AS (
    SELECT 0, 0, 1
    UNION ALL
    SELECT n + 1, b, a + b
    FROM fibonacci
    WHERE n < 10
)
SELECT n, a AS fibonacci_number
FROM fibonacci
''').fetchall()

print(result)