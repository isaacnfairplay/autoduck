# Generated: 2025-03-19 20:05:35.749828
# Result: [('Apple', datetime.date(2023, 1, 15), Decimal('100.50'), Decimal('100.50'), 100.5), ('Apple', datetime.date(2023, 1, 17), Decimal('125.75'), Decimal('226.25'), 113.125), ('Banana', datetime.date(2023, 1, 16), Decimal('75.25'), Decimal('75.25'), 75.25), ('Banana', datetime.date(2023, 1, 18), Decimal('90.00'), Decimal('165.25'), 82.625)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with temporal data and perform windowing
conn.execute('''CREATE TABLE sales (
    product STRING,
    sale_date DATE,
    amount DECIMAL(10,2)
);''')

conn.execute('''INSERT INTO sales VALUES
    ('Apple', '2023-01-15', 100.50),
    ('Banana', '2023-01-16', 75.25),
    ('Apple', '2023-01-17', 125.75),
    ('Banana', '2023-01-18', 90.00);
''')

# Calculate cumulative sales and running averages per product
result = conn.execute('''
    SELECT 
        product, 
        sale_date, 
        amount,
        SUM(amount) OVER (PARTITION BY product ORDER BY sale_date) as cumulative_sales,
        AVG(amount) OVER (PARTITION BY product ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as rolling_avg
    FROM sales
    ORDER BY product, sale_date
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Date: {row[1]}, Amount: ${row[2]}, Cumulative Sales: ${row[3]}, Rolling Avg: ${row[4]:.2f}")