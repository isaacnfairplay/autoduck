# Generated: 2025-03-19 19:46:16.250625
# Result: [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create recursive CTE to simulate factorial calculation
result = conn.execute('''
WITH RECURSIVE factorial(n, fact) AS (
    SELECT 1, 1
    UNION ALL
    SELECT n + 1, (n + 1) * fact FROM factorial WHERE n < 5
)
SELECT * FROM factorial
''').fetchall()

print(result)