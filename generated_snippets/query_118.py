# Generated: 2025-03-19 16:06:15.322765
# Result: [(0,), (1,), (1,), (2,), (3,), (5,), (8,), (13,), (21,), (34,), (55,)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Recursive Common Table Expression (CTE) to generate Fibonacci sequence
result = conn.execute('''
WITH RECURSIVE fibonacci(n, a, b) AS (
    SELECT 0, 0, 1
    UNION ALL
    SELECT n + 1, b, a + b
    FROM fibonacci
    WHERE n < 10
)
SELECT a AS fibonacci_number FROM fibonacci
''').fetchall()

print(result)  # Will print first 10 Fibonacci numbers