# Generated: 2025-03-19 10:09:51.566723
# Result: [('Tablet', datetime.datetime(2023, 1, 2, 14, 20), 2, 2), ('Laptop', datetime.datetime(2023, 1, 1, 10, 30), 5, 5), ('Laptop', datetime.datetime(2023, 1, 2, 9, 15), 7, 12), ('Phone', datetime.datetime(2023, 1, 1, 11, 45), 3, 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time series sales data with datetime
conn.execute('''
    CREATE TABLE sales_timeseries (
        date TIMESTAMP,
        product VARCHAR,
        quantity INTEGER,
        price DECIMAL(10,2)
    );

    INSERT INTO sales_timeseries VALUES
        ('2023-01-01 10:30:00', 'Laptop', 5, 999.99),
        ('2023-01-01 11:45:00', 'Phone', 3, 599.50),
        ('2023-01-02 09:15:00', 'Laptop', 7, 999.99),
        ('2023-01-02 14:20:00', 'Tablet', 2, 399.75)
''');

# Analyze sales time series with window functions
result = conn.execute('''
    SELECT 
        product, 
        date, 
        quantity,
        SUM(quantity) OVER (PARTITION BY product ORDER BY date) as cumulative_sales
    FROM sales_timeseries
''').fetchall()

for row in result:
    print(row)