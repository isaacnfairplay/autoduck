# Generated: 2025-03-19 12:04:51.248211
# Result: [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55)]
# Valid: True
import duckdb

# Create recursive CTE to generate Fibonacci sequence
conn = duckdb.connect(':memory:')

result = conn.execute('''
WITH RECURSIVE fibonacci(n, a, b) AS (
    SELECT 0, 0, 1
    UNION ALL
    SELECT n+1, b, a+b
    FROM fibonacci
    WHERE n < 10
)
SELECT n, a as fibonacci_number
FROM fibonacci
''').fetchall()

print(result)