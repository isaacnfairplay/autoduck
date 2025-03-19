# Generated: 2025-03-19 08:24:20.970214
# Result: [('Clothing', 'Jacket', Decimal('250.75'), Decimal('250.75')), ('Electronics', 'Smartphone', Decimal('800.25'), Decimal('800.25')), ('Electronics', 'Laptop', Decimal('1200.50'), Decimal('2000.75'))]
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
    SUM(sale_amount) OVER (PARTITION BY category ORDER BY sale_amount) as cumulative_category_sales
FROM product_sales
ORDER BY category, cumulative_category_sales
''').fetchall()

for row in result:
    print(row)