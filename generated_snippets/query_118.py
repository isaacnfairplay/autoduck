# Generated: 2025-03-19 19:35:08.282323
# Result: [('2023-01-01', Decimal('1200.50'), 1200.5), ('2023-01-02', Decimal('1350.75'), 1275.625), ('2023-01-03', Decimal('1100.25'), 1217.1666666666667)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time series sales data
conn.execute('''
CREATE TABLE daily_sales AS
SELECT '2023-01-01' as sales_date, 1200.50 as revenue
UNION ALL SELECT '2023-01-02', 1350.75
UNION ALL SELECT '2023-01-03', 1100.25
''')

# Calculate 3-day moving average of revenue
result = conn.execute('''
SELECT 
    sales_date, 
    revenue,
    AVG(revenue) OVER (ORDER BY sales_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg
FROM daily_sales
''').fetchall()

print(result)