# Generated: 2025-03-19 19:41:06.003429
# Result: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a self-referencing recursive CTE to generate numeric sequences
result = conn.execute('''
WITH RECURSIVE number_sequence(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM number_sequence WHERE n < 10
)
SELECT * FROM number_sequence
''').fetchall()

print(result)