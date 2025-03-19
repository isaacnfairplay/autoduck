# Generated: 2025-03-19 14:14:46.915520
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

print([row[0] for row in result])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]