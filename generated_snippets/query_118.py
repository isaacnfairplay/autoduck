# Generated: 2025-03-19 08:50:37.326211
# Result: [('Laptop', Decimal('1200.50'), 'Electronics'), ('Phone', Decimal('800.25'), 'Electronics')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with product sales data
conn.execute('CREATE TABLE products (id INT, name TEXT, price DECIMAL(10,2), category TEXT)')
conn.executemany('INSERT INTO products VALUES (?, ?, ?, ?)', [
    (1, 'Laptop', 1200.50, 'Electronics'),
    (2, 'Phone', 800.25, 'Electronics'),
    (3, 'Book', 25.99, 'Literature')
])

# Perform SELECT with multiple conditions and ordering
result = conn.execute('''
    SELECT name, price, category 
    FROM products 
    WHERE category = 'Electronics' AND price > 700 
    ORDER BY price DESC
''').fetchall()

for row in result:
    print(f'Product: {row[0]}, Price: ${row[1]}, Category: {row[2]}')