# Generated: 2025-03-19 10:00:02.118946
# Result: [('2023-01-01', Decimal('500.50'), 500.5), ('2023-01-02', Decimal('250.75'), 375.625), ('2023-01-03', Decimal('1200.00'), 650.4166666666666), ('2023-01-04', Decimal('750.25'), 733.6666666666666)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time series sales data
conn.execute('''
CREATE TABLE daily_sales AS
SELECT * FROM (
    VALUES
    ('2023-01-01', 500.50),
    ('2023-01-02', 250.75),
    ('2023-01-03', 1200.00),
    ('2023-01-04', 750.25)
) t(sale_date, amount)
''')

# Calculate 3-day moving average of sales
result = conn.execute('''
SELECT 
    sale_date, 
    amount,
    AVG(amount) OVER (
        ORDER BY sale_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) as rolling_3day_avg
FROM daily_sales
''').fetchall()

for row in result:
    print(row)