# Generated: 2025-03-19 19:56:39.958803
# Result: [('Electronics', 'Computers', Decimal('2100.00'), 1), ('Clothing', 'Tops', Decimal('600.00'), 2), ('Clothing', 'Outerwear', Decimal('800.00'), 1), ('Electronics', 'Mobile', Decimal('1500.00'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table with multi-category hierarchical data
conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    subcategory VARCHAR,
    product_name VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
('Electronics', 'Computers', 'Laptop', 1200),
('Electronics', 'Computers', 'Desktop', 900),
('Electronics', 'Mobile', 'Smartphone', 1500),
('Clothing', 'Outerwear', 'Jacket', 800),
('Clothing', 'Tops', 'Shirt', 600);
'''
)

# Demonstrate multi-level aggregation and window ranking
result = conn.execute('''
SELECT 
    category, 
    subcategory, 
    SUM(sales_amount) as total_subcategory_sales,
    RANK() OVER (PARTITION BY category ORDER BY SUM(sales_amount) DESC) as subcategory_rank
FROM product_sales
GROUP BY category, subcategory
QUALIFY subcategory_rank <= 2
''').fetchall()

print(result)