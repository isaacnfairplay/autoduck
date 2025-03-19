# Generated: 2025-03-19 09:16:49.361156
# Result: [('Phone', Decimal('200062.50'), 800.25), ('Laptop', Decimal('120050.00'), 1200.5), ('Tablet', Decimal('45000.00'), 600.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a product sales tracking table
conn.execute('CREATE TABLE sales (product TEXT, quantity INT, price DECIMAL(10,2))')

# Insert sample sales data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('Laptop', 100, 1200.50),
    ('Phone', 250, 800.25),
    ('Tablet', 75, 600.00)
])

# Calculate total sales amount per product
result = conn.execute('''
    SELECT 
        product, 
        SUM(quantity * price) as total_revenue,
        AVG(price) as average_price
    FROM sales
    GROUP BY product
    ORDER BY total_revenue DESC
''').fetchall()

for row in result:
    print(f'Product: {row[0]}, Total Revenue: ${row[1]}, Avg Price: ${row[2]:.2f}')