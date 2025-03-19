# Generated: 2025-03-19 09:08:52.390492
# Result: [('Smartphone', 'Mobile Devices', Decimal('799.99'))]
# Valid: True
# Variable product: Type: tuple
# Attributes/Methods: count, index
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics catalog table
conn.execute('CREATE TABLE electronics (product_id INT, name TEXT, category TEXT, price DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO electronics VALUES (?, ?, ?, ?)', [
    (1, 'Smartphone', 'Mobile Devices', 799.99),
    (2, 'Laptop', 'Computers', 1299.50),
    (3, 'Tablet', 'Mobile Devices', 499.99)
])

# Query mobile devices above specified price threshold
result = conn.execute(
    'SELECT name, category, price FROM electronics WHERE category = ? AND price > ?', 
    ('Mobile Devices', 600)
).fetchall()

for product in result:
    print(f'Product: {product[0]}, Category: {product[1]}, Price: ${product[2]}')