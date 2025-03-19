# Generated: 2025-03-19 12:42:22.752909
# Result: [('Electronics', 2, Decimal('2000.00'), 1000.0), ('Clothing', 1, Decimal('50.00'), 50.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE product_sales (
    product VARCHAR,
    category VARCHAR,
    sale_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
    ('Laptop', 'Electronics', 1200.00),
    ('Smartphone', 'Electronics', 800.00),
    ('Shirt', 'Clothing', 50.00);
''')

# Analyze total sales by category
result = conn.execute('''
SELECT
    category,
    COUNT(*) as product_count,
    SUM(sale_amount) as total_sales,
    AVG(sale_amount) as avg_sale
FROM product_sales
GROUP BY category
''').fetchall()

for row in result:
    print(row)