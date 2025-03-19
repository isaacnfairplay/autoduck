# Generated: 2025-03-19 12:35:30.603637
# Result: [('Laptop', 'Electronics', Decimal('1200.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR,
    category VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
    (1, 'Laptop', 'Electronics', 1200.00),
    (2, 'Shirt', 'Clothing', 50.00),
    (3, 'Chair', 'Furniture', 250.50);
''')

result = conn.execute('''
SELECT name, category, price
FROM products
WHERE category = 'Electronics' AND price > 1000
''').fetchall()

for row in result:
    print(row)