# Generated: 2025-03-18 22:08:15.776990
# Result: [('Electronics', 'Laptop', Decimal('999.99'), 799.99, 1), ('Electronics', 'Smartphone', Decimal('599.99'), 799.99, 2), ('Sports', 'Running Shoes', Decimal('129.99'), 129.99, 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.sql('''
CREATE TABLE products (
    category VARCHAR,
    name VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
    ('Electronics', 'Laptop', 1200.00),
    ('Electronics', 'Smartphone', 800.00),
    ('Clothing', 'Shirt', 50.00);

SELECT 
    category, 
    name, 
    price,
    MAX(price) OVER (PARTITION BY category) as max_category_price
FROM products
''').show()