# Generated: 2025-03-19 08:15:19.215790
# Result: [('Clothing', 'Pants', Decimal('100.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
    ('Clothing', 'Shirt', 50.00),
    ('Clothing', 'Pants', 100.00);
''')

result = conn.execute('''
SELECT * FROM product_sales
WHERE category = 'Clothing' AND product = 'Pants'
''').fetchall()

for row in result:
    print(row)