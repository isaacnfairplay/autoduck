# Generated: 2025-03-19 10:45:52.533478
# Result: [(datetime.date(2023, 1, 1),), (datetime.date(2023, 1, 2),), (datetime.date(2023, 1, 3),), (datetime.date(2023, 1, 4),), (datetime.date(2023, 1, 5),), (datetime.date(2023, 1, 6),), (datetime.date(2023, 1, 7),), (datetime.date(2023, 1, 8),), (datetime.date(2023, 1, 9),), (datetime.date(2023, 1, 10),)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Generate a date series with date constraint
result = conn.execute("""WITH RECURSIVE date_series AS (
    SELECT DATE '2023-01-01' AS generated_date
    UNION ALL
    SELECT generated_date + INTERVAL 1 DAY
    FROM date_series
    WHERE generated_date < DATE '2023-01-10'
)
SELECT generated_date
FROM date_series""").fetchall()

print([str(date[0]) for date in result])