# Generated: 2025-03-19 08:21:45.127000
# Result: [('Electronics', 2, Decimal('2000.75'), 1000.375), ('Clothing', 1, Decimal('250.75'), 250.75)]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create product sales table with category focus
conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
    ('Electronics', 'Laptop', 1200.50),
    ('Electronics', 'Smartphone', 800.25),
    ('Clothing', 'Jacket', 250.75);
''')

# Analyze sales by category
result = conn.execute('''
SELECT 
    category, 
    COUNT(*) as product_count,
    SUM(sales_amount) as total_category_sales,
    AVG(sales_amount) as avg_category_sales
FROM product_sales
GROUP BY category
ORDER BY total_category_sales DESC
''').fetchall()

for row in result:
    print(row)