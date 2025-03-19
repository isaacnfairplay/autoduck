# Generated: 2025-03-19 08:22:36.243290
# Result: [('Laptop', Decimal('1200.50'), 'Electronics'), ('Smartphone', Decimal('800.25'), 'Electronics'), ('Tablet', Decimal('500.00'), 'Electronics')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE products (
    product_id INT,
    name VARCHAR,
    price DECIMAL(10,2),
    category VARCHAR
);

INSERT INTO products VALUES
    (1, 'Laptop', 1200.50, 'Electronics'),
    (2, 'Smartphone', 800.25, 'Electronics'),
    (3, 'Tablet', 500.00, 'Electronics');
''')

result = conn.execute('''
SELECT name, price, category
FROM products
WHERE category = 'Electronics'
ORDER BY price DESC
''').fetchall()

for row in result:
    print(row)