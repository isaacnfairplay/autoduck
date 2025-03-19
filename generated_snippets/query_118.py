# Generated: 2025-03-19 17:30:00.956411
# Result: [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Recursive common table expression (CTE) to generate fibonacci sequence
result = conn.execute('''
WITH RECURSIVE fibonacci(n, a, b) AS (
    SELECT 1, 0, 1
    UNION ALL
    SELECT n+1, b, a+b FROM fibonacci WHERE n < 10
)
SELECT n, b AS fibonacci_number FROM fibonacci
''').fetchall()

for row in result:
    print(row)