# Generated: 2025-03-19 18:20:29.474386
# Result: (10, 34)
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Recursive common table expression to generate a Fibonacci sequence
query = '''
WITH RECURSIVE fibonacci(n, a, b) AS (
    SELECT 1, 0, 1
    UNION ALL
    SELECT n + 1, b, a + b
    FROM fibonacci
    WHERE n < 10
)
SELECT n, a AS fibonacci_number
FROM fibonacci;
'''

results = conn.execute(query).fetchall()
for result in results:
    print(f'Position {result[0]}: {result[1]}')