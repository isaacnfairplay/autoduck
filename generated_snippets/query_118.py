# Generated: 2025-03-19 08:27:54.032615
# Result: [('Laptop', Decimal('1200.50')), ('Smartphone', Decimal('800.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE products (
    id INTEGER,
    name VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
    (1, 'Laptop', 1200.50),
    (2, 'Smartphone', 800.25),
    (3, 'Tablet', 500.00);
''')

result = conn.execute('''
SELECT name, price
FROM products
WHERE price > 600
ORDER BY price DESC
''').fetchall()

for row in result:
    print(row)