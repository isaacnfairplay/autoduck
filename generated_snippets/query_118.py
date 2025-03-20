# Generated: 2025-03-19 20:12:21.849468
# Result: [('Laptop', 50, Decimal('999.99'), Decimal('49999.50'), Decimal('136198.75')), ('Smartphone', 100, Decimal('599.50'), Decimal('59950.00'), Decimal('136198.75')), ('Tablet', 75, Decimal('349.99'), Decimal('26249.25'), Decimal('136198.75'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with product inventory
conn.execute('''CREATE TABLE inventory (
    product_id INTEGER,
    product_name STRING,
    quantity INTEGER,
    price DECIMAL(10,2)
)''')

conn.execute('''INSERT INTO inventory VALUES
    (1, 'Laptop', 50, 999.99),
    (2, 'Smartphone', 100, 599.50),
    (3, 'Tablet', 75, 349.99)''')

# Calculate total inventory value using window function
result = conn.execute('''SELECT 
    product_name, 
    quantity, 
    price, 
    quantity * price AS total_value,
    SUM(quantity * price) OVER () AS grand_total_inventory
FROM inventory''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Quantity: {row[1]}, Price: ${row[2]}, Total Value: ${row[3]}, Grand Total Inventory: ${row[4]:.2f}")