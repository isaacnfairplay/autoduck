# Generated: 2025-03-19 19:53:12.719699
# Result: [('Electronics', 'Phone', Decimal('1500.00')), ('Electronics', 'Laptop', Decimal('1200.00')), ('Clothing', 'Pants', Decimal('950.00')), ('Electronics', 'Tablet', Decimal('900.00')), ('Clothing', 'Shirt', Decimal('800.00'))]
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
('Clothing', 'Shirt', 800),
('Clothing', 'Pants', 950);
''')

# Calculate total sales by category and product
result = conn.execute('''
SELECT 
    category, 
    product_name,
    SUM(sales_amount) as total_product_sales
FROM product_sales
GROUP BY category, product_name
ORDER BY total_product_sales DESC
''').fetchall()

print(result)