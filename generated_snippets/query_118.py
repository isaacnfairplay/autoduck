# Generated: 2025-03-19 10:31:24.537254
# Result: [(datetime.date(2023, 1, 1), 'Widget', Decimal('100.000'), 100.0), (datetime.date(2023, 1, 2), 'Widget', Decimal('150.000'), 125.0), (datetime.date(2023, 1, 3), 'Widget', Decimal('200.000'), 150.0), (datetime.date(2023, 1, 4), 'Widget', Decimal('180.000'), 176.66666666666666)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Generate a series of dates using recursive CTE
conn.execute("""
WITH RECURSIVE date_series(date) AS (
    SELECT DATE '2023-01-01'
    UNION ALL
    SELECT date + INTERVAL 1 DAY
    FROM date_series
    WHERE date < DATE '2023-01-10'
)
SELECT * FROM date_series
""")

results = conn.fetchall()
for row in results:
    print(row[0])