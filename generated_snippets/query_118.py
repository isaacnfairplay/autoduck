# Generated: 2025-03-19 12:33:47.991122
# Result: [(3, 'Electronics', Decimal('1200.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create products table
conn.execute('''
CREATE TABLE products (
    product_id INT,
    category VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
    (1, 'Electronics', 500.00),
    (2, 'Clothing', 75.50),
    (3, 'Electronics', 1200.00);
''')

# Select specific columns with condition
result = conn.execute('''
SELECT product_id, category, price
FROM products
WHERE category = 'Electronics' AND price > 750
''').fetchall()

for row in result:
    print(row)