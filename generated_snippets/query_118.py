# Generated: 2025-03-19 09:03:41.145146
# Result: (Decimal('185050.00'), 866.9166666666666)
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product inventory table
conn.execute('CREATE TABLE inventory (product_id INT, product_name TEXT, stock INT, price DECIMAL(10,2))')

# Insert sample inventory data
conn.executemany('INSERT INTO inventory VALUES (?, ?, ?, ?)', [
    (1, 'Laptop', 50, 1200.50),
    (2, 'Phone', 100, 800.25),
    (3, 'Tablet', 75, 600.00)
])

# Calculate total inventory value using SQL aggregation
result = conn.execute('''SELECT 
    SUM(stock * price) as total_inventory_value, 
    AVG(price) as average_product_price 
FROM inventory''').fetchone()

print(f'Total Inventory Value: ${result[0]}, Average Product Price: ${result[1]}')