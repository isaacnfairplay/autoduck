# Generated: 2025-03-19 09:14:11.476071
# Result: [('Laptop', Decimal('1200.50')), ('Phone', Decimal('800.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate products table
conn.execute('CREATE TABLE products (id INT, name TEXT, price DECIMAL(10,2))')
conn.executemany('INSERT INTO products VALUES (?, ?, ?)', [
    (1, 'Laptop', 1200.50),
    (2, 'Phone', 800.25),
    (3, 'Tablet', 600.00)
])

# Demonstrate SELECT with complex filtering and projection
result = conn.execute(
    'SELECT name, price FROM products WHERE price > 700 ORDER BY price DESC'
).fetchall()

for product in result:
    print(f'Product: {product[0]}, Price: ${product[1]}')