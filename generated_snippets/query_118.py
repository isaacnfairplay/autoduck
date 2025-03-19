# Generated: 2025-03-19 08:23:28.033465
# Result: [('Electronics', Decimal('2000.75')), ('Clothing', Decimal('250.75'))]
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
SELECT category, SUM(sale_amount) as total_sales
FROM product_sales
GROUP BY category
ORDER BY total_sales DESC
''').fetchall()

for row in result:
    print(row)