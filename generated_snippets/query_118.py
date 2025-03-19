# Generated: 2025-03-19 18:02:29.631034
# Result: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Recursive common table expression (CTE) to generate a numeric sequence
result = conn.execute('''
    WITH RECURSIVE number_series(n) AS (
        SELECT 1
        UNION ALL
        SELECT n + 1 FROM number_series WHERE n < 10
    )
    SELECT * FROM number_series
''').fetchall()

print(result)  # Demonstrates recursive query for generating sequential numbers