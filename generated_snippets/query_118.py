# Generated: 2025-03-19 08:14:28.122318
# Result: [('Clothing', 'Shirt', Decimal('50.00'))]
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
    ('Clothing', 'Shirt', 50.00);
''')

result = conn.execute('''
SELECT * FROM product_sales
WHERE category = 'Clothing' AND product = 'Shirt'
''').fetchall()

for row in result:
    print(row)