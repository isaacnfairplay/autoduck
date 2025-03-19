# Generated: 2025-03-19 10:38:19.497527
# Result: [(datetime.date(2024, 1, 1),), (datetime.date(2024, 1, 8),), (datetime.date(2024, 1, 15),), (datetime.date(2024, 1, 22),), (datetime.date(2024, 1, 29),), (datetime.date(2024, 2, 5),), (datetime.date(2024, 2, 12),), (datetime.date(2024, 2, 19),), (datetime.date(2024, 2, 26),), (datetime.date(2024, 3, 4),), (datetime.date(2024, 3, 11),), (datetime.date(2024, 3, 18),), (datetime.date(2024, 3, 25),), (datetime.date(2024, 4, 1),)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Generate a weekly date series for 2024 fiscal quarters
result = conn.execute("""
WITH RECURSIVE date_series AS (
    SELECT DATE '2024-01-01' AS generated_date
    UNION ALL
    SELECT generated_date + INTERVAL 7 DAYS
    FROM date_series
    WHERE generated_date < DATE '2024-04-01'
)
SELECT generated_date
FROM date_series
""").fetchall()

print([date[0] for date in result])