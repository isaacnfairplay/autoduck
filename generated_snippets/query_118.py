# Generated: 2025-03-19 12:38:56.185648
# Result: [('Laptop', 'Electronics', Decimal('1200.00'), 1000.0), ('Smartphone', 'Electronics', Decimal('800.00'), 1000.0), ('Shirt', 'Clothing', Decimal('50.00'), 62.5), ('Pants', 'Clothing', Decimal('75.00'), 62.5)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE product_sales (
    product VARCHAR,
    category VARCHAR,
    amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
    ('Laptop', 'Electronics', 1200.00),
    ('Smartphone', 'Electronics', 800.00),
    ('Shirt', 'Clothing', 50.00),
    ('Pants', 'Clothing', 75.00)
''');

result = conn.execute('''
SELECT 
    product, 
    category, 
    amount,
    (SELECT AVG(amount) FROM product_sales ps WHERE ps.category = product_sales.category) as category_avg
FROM product_sales
''').fetchall();

for row in result:
    print(row)