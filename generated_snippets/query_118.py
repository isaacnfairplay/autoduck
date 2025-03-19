# Generated: 2025-03-19 12:38:05.233816
# Result: [('Laptop', 'Electronics', Decimal('1200.00'), 1), ('Smartphone', 'Electronics', Decimal('800.00'), 2), ('Chair', 'Furniture', Decimal('250.50'), 1), ('Pants', 'Clothing', Decimal('75.00'), 1), ('Shirt', 'Clothing', Decimal('50.00'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE sales (
    product VARCHAR,
    category VARCHAR,
    amount DECIMAL(10,2)
);

INSERT INTO sales VALUES
    ('Laptop', 'Electronics', 1200.00),
    ('Smartphone', 'Electronics', 800.00),
    ('Shirt', 'Clothing', 50.00),
    ('Pants', 'Clothing', 75.00),
    ('Chair', 'Furniture', 250.50)
''')

result = conn.execute('''
SELECT 
    product, 
    category, 
    amount,
    RANK() OVER (PARTITION BY category ORDER BY amount DESC) as category_rank
FROM sales
''').fetchall()

for row in result:
    print(row)