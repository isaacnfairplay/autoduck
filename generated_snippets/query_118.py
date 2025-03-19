# Generated: 2025-03-18 23:30:06.090864
# Result: [('Electronics', 'Laptop', Decimal('999.99'), 799.99, 1), ('Electronics', 'Smartphone', Decimal('599.99'), 799.99, 2), ('Sports', 'Running Shoes', Decimal('129.99'), 129.99, 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.sql('''
CREATE TABLE clothing_items (
    id INTEGER,
    name VARCHAR,
    price DECIMAL(10,2),
    size VARCHAR
);

INSERT INTO clothing_items VALUES
    (1, 'Shirt', 50.00, 'M'),
    (2, 'Shirt', 55.00, 'L'),
    (3, 'Shirt', 45.00, 'S');

SELECT 
    name, 
    size, 
    price,
    RANK() OVER (ORDER BY price) as price_rank
FROM clothing_items
''').show()