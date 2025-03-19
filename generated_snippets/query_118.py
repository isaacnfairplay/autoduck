# Generated: 2025-03-19 10:40:08.486712
# Result: [(datetime.date(2024, 1, 1),), (datetime.date(2024, 2, 1),), (datetime.date(2024, 3, 1),), (datetime.date(2024, 4, 1),), (datetime.date(2024, 5, 1),), (datetime.date(2024, 6, 1),), (datetime.date(2024, 7, 1),), (datetime.date(2024, 8, 1),), (datetime.date(2024, 9, 1),), (datetime.date(2024, 10, 1),), (datetime.date(2024, 11, 1),), (datetime.date(2024, 12, 1),), (datetime.date(2025, 1, 1),)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Generate monthly fiscal date series for 2024 with start and end bounds
result = conn.execute("""
WITH RECURSIVE date_series(fiscal_month) AS (
    SELECT DATE '2024-01-01'
    UNION ALL
    SELECT fiscal_month + INTERVAL 1 MONTH
    FROM date_series
    WHERE fiscal_month < DATE '2024-12-31'
)
SELECT fiscal_month
FROM date_series
""").fetchall()

print([str(date[0]) for date in result])