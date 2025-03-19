# Generated: 2025-03-19 09:09:43.098142
# Result: [('Smartphone', 'Electronics', Decimal('799.99')), ('Laptop', 'Electronics', Decimal('1299.50'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics catalog table
conn.execute('CREATE TABLE electronics (product_id INT, name TEXT, category TEXT, price DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO electronics VALUES (?, ?, ?, ?)', [
    (1, 'Smartphone', 'Electronics', 799.99),
    (2, 'Laptop', 'Electronics', 1299.50),
    (3, 'Tablet', 'Electronics', 499.99)
])

# Query specific electronics category with price filter
result = conn.execute(
    'SELECT name, category, price FROM electronics WHERE category = ? AND price >= ?', 
    ('Electronics', 500)
).fetchall()

for product in result:
    print(f'Product: {product[0]}, Category: {product[1]}, Price: ${product[2]}')