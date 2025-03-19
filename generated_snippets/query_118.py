# Generated: 2025-03-19 08:30:31.030986
# Result: [('Clothing', 'Jacket', Decimal('250.75'), Decimal('250.75'), 1), ('Electronics', 'Laptop', Decimal('1200.50'), Decimal('2000.75'), 1), ('Electronics', 'Smartphone', Decimal('800.25'), Decimal('800.25'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product VARCHAR,
    sale_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
    ('Electronics', 'Laptop', 1200.50),
    ('Electronics', 'Smartphone', 800.25),
    ('Clothing', 'Jacket', 250.75);
''')

result = conn.execute('''
SELECT 
    category, 
    product, 
    sale_amount,
    SUM(sale_amount) OVER (PARTITION BY category ORDER BY sale_amount) as cumulative_category_sales,
    RANK() OVER (PARTITION BY category ORDER BY sale_amount DESC) as product_rank
FROM product_sales
ORDER BY category, product_rank
''').fetchall()

for row in result:
    print(row)