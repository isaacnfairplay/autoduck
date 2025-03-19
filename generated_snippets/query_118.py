# Generated: 2025-03-19 10:45:01.975333
# Result: [(datetime.date(2024, 1, 1),), (datetime.date(2024, 4, 1),), (datetime.date(2024, 7, 1),), (datetime.date(2024, 10, 1),), (datetime.date(2025, 1, 1),)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Generate quarterly fiscal date series for 2024
result = conn.execute("""
WITH RECURSIVE date_series(fiscal_quarter) AS (
    SELECT DATE '2024-01-01'
    UNION ALL
    SELECT fiscal_quarter + INTERVAL 3 MONTH
    FROM date_series
    WHERE fiscal_quarter < DATE '2024-12-31'
)
SELECT fiscal_quarter
FROM date_series
""").fetchall()

print([str(date[0]) for date in result])