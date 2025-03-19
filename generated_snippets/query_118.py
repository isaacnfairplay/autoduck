# Generated: 2025-03-19 19:57:30.926342
# Result: [('Electronics', 'Phone', Decimal('1500.00'), 1), ('Electronics', 'Laptop', Decimal('1200.00'), 2), ('Clothing', 'Pants', Decimal('950.00'), 1), ('Clothing', 'Shirt', Decimal('800.00'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product_name VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
('Electronics', 'Laptop', 1200),
('Electronics', 'Phone', 1500),
('Electronics', 'Tablet', 900),
('Clothing', 'Shirt', 800),
('Clothing', 'Pants', 950);
''')

result = conn.execute('''
SELECT category, product_name, sales_amount,
       RANK() OVER (PARTITION BY category ORDER BY sales_amount DESC) as sales_rank
FROM product_sales
QUALIFY sales_rank <= 2
''').fetchall()

print(result)