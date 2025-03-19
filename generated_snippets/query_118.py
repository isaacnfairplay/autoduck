# Generated: 2025-03-19 08:57:31.667788
# Result: [('Laptop', datetime.date(2023, 7, 1), 5, 5, Decimal('6002.50')), ('Phone', datetime.date(2023, 7, 2), 3, 8, Decimal('8403.25')), ('Tablet', datetime.date(2023, 7, 3), 2, 10, Decimal('9404.75'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table for tracking product orders
conn.execute('CREATE TABLE product_orders (product TEXT, order_date DATE, quantity INT, price DECIMAL(10,2))')

# Insert sample order data
conn.executemany('INSERT INTO product_orders VALUES (?, ?, ?, ?)', [
    ('Laptop', '2023-07-01', 5, 1200.50),
    ('Phone', '2023-07-02', 3, 800.25),
    ('Tablet', '2023-07-03', 2, 500.75)
])

# Calculate cumulative quantity and total value using window functions
result = conn.execute('''  
    SELECT 
        product, 
        order_date, 
        quantity,
        SUM(quantity) OVER (ORDER BY order_date) as cumulative_quantity,
        SUM(quantity * price) OVER (ORDER BY order_date) as cumulative_value
    FROM product_orders
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Date: {row[1]}, Quantity: {row[2]}, Cumulative Qty: {row[3]}, Cumulative Value: ${row[4]:.2f}")