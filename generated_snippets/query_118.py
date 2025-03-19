# Generated: 2025-03-19 15:40:01.739661
# Result: [(datetime.date(2023, 1, 1), 100, 100.0, 100), (datetime.date(2023, 1, 2), 120, 110.0, 220), (datetime.date(2023, 1, 3), 110, 110.0, 330), (datetime.date(2023, 1, 4), 130, 120.0, 460), (datetime.date(2023, 1, 5), 140, 126.66666666666667, 600)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Complex temporal trend analysis with time series aggregation
result = conn.sql('''
    WITH daily_sales AS (
        SELECT DATE '2023-01-01' as sale_date, 100 as revenue
        UNION ALL SELECT DATE '2023-01-02', 120
        UNION ALL SELECT DATE '2023-01-03', 110
        UNION ALL SELECT DATE '2023-01-04', 130
        UNION ALL SELECT DATE '2023-01-05', 140
    )
    SELECT 
        sale_date,
        revenue,
        AVG(revenue) OVER (ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg,
        SUM(revenue) OVER (ORDER BY sale_date ROWS UNBOUNDED PRECEDING) as cumulative_revenue
    FROM daily_sales
''').fetchall()

print(result)