# Generated: 2025-03-19 13:11:46.709875
# Result: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a recursive Common Table Expression (CTE) to generate a sequence
result = conn.execute('''
WITH RECURSIVE sequence(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM sequence WHERE n < 10
)
SELECT * FROM sequence
''').fetchall()

print(result)  # Will print numbers 1 through 10