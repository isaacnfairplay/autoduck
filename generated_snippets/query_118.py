# Generated: 2025-03-19 15:18:33.213167
# Result: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Recursive Common Table Expression (CTE) to generate sequence
result = conn.execute('''
    WITH RECURSIVE number_sequence(n) AS (
        SELECT 1
        UNION ALL
        SELECT n + 1 FROM number_sequence WHERE n < 10
    )
    SELECT n, n * n AS squared FROM number_sequence
''').fetchall()

print(result)  # Generates numbers 1-10 with their squares using recursive CTE