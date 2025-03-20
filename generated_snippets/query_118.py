# Generated: 2025-03-19 21:13:54.829638
# Result: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Recursive common table expression to generate number series
result = conn.sql("""
WITH RECURSIVE number_series(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM number_series WHERE n < 10
)
SELECT * FROM number_series
""").fetchall()

print(result)