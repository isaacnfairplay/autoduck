# Generated: 2025-03-19 13:45:02.859957
# Result: [('Laptop', datetime.date(2023, 1, 15), Decimal('4999.95'), 1), ('Phone', datetime.date(2023, 1, 15), Decimal('4995.00'), 2), ('Tablet', datetime.date(2023, 1, 16), Decimal('2098.25'), 3)]
# Valid: True
import duckdb

# Create in-memory database and generate product sales analysis
conn = duckdb.connect(':memory:')

# Create sales table with timestamps
conn.execute('CREATE TABLE product_sales (product VARCHAR, sale_timestamp TIMESTAMP, quantity INT, price DECIMAL(10,2))')

# Insert sample time-based sales data
conn.executemany('INSERT INTO product_sales VALUES (?, ?, ?, ?)', [
    ('Laptop', '2023-01-15 10:30:00', 5, 999.99),
    ('Phone', '2023-01-15 11:45:00', 10, 499.50),
    ('Tablet', '2023-01-16 09:20:00', 7, 299.75)
])

# Perform time-window aggregation and ranking
result = conn.execute('''
    SELECT 
        product,
        DATE_TRUNC('day', sale_timestamp) as sale_day,
        SUM(quantity * price) as daily_revenue,
        RANK() OVER (ORDER BY SUM(quantity * price) DESC) as revenue_rank
    FROM product_sales
    GROUP BY product, sale_day
''').fetchall()

print(result)