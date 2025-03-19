# Generated: 2025-03-19 16:00:17.305490
# Result: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a recursive common table expression (CTE) to generate a sequence
result = conn.execute('''WITH RECURSIVE number_sequence(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM number_sequence WHERE n < 10
)
SELECT * FROM number_sequence''').fetchall()

print([row[0] for row in result])