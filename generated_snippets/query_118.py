# Generated: 2025-03-19 19:45:25.640664
# Result: [('Electronics', 'Phone', Decimal('2300.00')), ('Electronics', 'Laptop', Decimal('1200.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table
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
('Electronics', 'Phone', 800);
''')

# Demonstrate grouped aggregation with multiple conditions
result = conn.execute('''
SELECT 
    category, 
    product_name, 
    SUM(sales_amount) as total_product_sales
FROM product_sales
GROUP BY category, product_name
HAVING total_product_sales > 1000
''').fetchall()

print(result)