# Generated: 2025-03-19 10:51:05.553356
# Result: [(datetime.date(2024, 1, 1),), (datetime.date(2024, 1, 8),), (datetime.date(2024, 1, 15),), (datetime.date(2024, 1, 22),), (datetime.date(2024, 1, 29),), (datetime.date(2024, 2, 5),)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Generate a weekly fiscal date series using recursive CTE
result = conn.execute("""
WITH RECURSIVE date_series AS (
    SELECT DATE '2024-01-01' AS fiscal_week
    UNION ALL
    SELECT fiscal_week + INTERVAL 7 DAYS
    FROM date_series
    WHERE fiscal_week < DATE '2024-02-01'
)
SELECT fiscal_week
FROM date_series
""").fetchall()

print([str(date[0]) for date in result])