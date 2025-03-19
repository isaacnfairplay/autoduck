# Generated: 2025-03-19 19:05:03.827745
# Result: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create recursive common table expression to generate Fibonacci sequence
result = conn.sql("""
WITH RECURSIVE fibonacci(n, a, b) AS (
    SELECT 0, 0, 1
    UNION ALL
    SELECT n + 1, b, a + b
    FROM fibonacci
    WHERE n < 10
)
SELECT n, b AS fibonacci_number FROM fibonacci
""").fetchall()

for row in result:
    print(f"Iteration {row[0]}: {row[1]}")