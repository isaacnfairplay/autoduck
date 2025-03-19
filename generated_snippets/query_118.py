# Generated: 2025-03-19 16:31:08.633362
# Result: [(0,), (1,), (1,), (2,), (3,), (5,), (8,), (13,), (21,), (34,)]
# Valid: True
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create a recursive common table expression to generate a Fibonacci sequence
result = conn.execute('''
WITH RECURSIVE fibonacci(n, current, next) AS (
    SELECT 1, 0, 1
    UNION ALL
    SELECT n + 1, next, current + next
    FROM fibonacci
    WHERE n < 10
)
SELECT current AS fibonacci_number FROM fibonacci
''').fetchall()

for row in result:
    print(row)