# Generated: 2025-03-19 19:43:42.063393
# Result: [('Electronics', Decimal('3600.00'))]
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
('Electronics', 'Tablet', 900);
''')

# Calculate total sales by category
result = conn.execute('''
SELECT category, 
       SUM(sales_amount) as total_category_sales
FROM product_sales
GROUP BY category
''').fetchall()

print(result)