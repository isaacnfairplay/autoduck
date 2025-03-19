# Generated: 2025-03-19 10:30:30.203581
# Result: [(datetime.date(2023, 1, 1), 'Widget', Decimal('100.000'), 100.0), (datetime.date(2023, 1, 2), 'Widget', Decimal('150.000'), 125.0), (datetime.date(2023, 1, 3), 'Widget', Decimal('200.000'), 150.0), (datetime.date(2023, 1, 4), 'Widget', Decimal('180.000'), 176.66666666666666)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales data with dates
conn.execute('''
    CREATE TABLE sales (date DATE, product TEXT, amount DECIMAL);
    INSERT INTO sales VALUES 
        ('2023-01-01', 'Widget', 100),
        ('2023-01-02', 'Widget', 150),
        ('2023-01-03', 'Widget', 200),
        ('2023-01-04', 'Widget', 180)
''');

# Calculate 3-day rolling average
result = conn.execute('''
    SELECT 
        date, 
        product, 
        amount,
        AVG(amount) OVER (
            PARTITION BY product 
            ORDER BY date 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS rolling_avg
    FROM sales
''').fetchall()

for row in result:
    print(row)