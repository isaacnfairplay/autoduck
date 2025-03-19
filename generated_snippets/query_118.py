# Generated: 2025-03-19 08:33:12.903506
# Result: [('Electronics', 'Smartphone', 800, 75, 1, 75), ('Electronics', 'Laptop', 1200, 50, 2, 125), ('Clothing', 'Shirt', 50, 100, 1, 100), ('Clothing', 'Jeans', 80, 60, 2, 160)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data
conn.execute('''
CREATE TABLE product_sales AS
SELECT 'Electronics' as category, 'Laptop' as product, 1200 as price, 50 as quantity
UNION ALL
SELECT 'Electronics', 'Smartphone', 800, 75
UNION ALL
SELECT 'Clothing', 'Shirt', 50, 100
UNION ALL
SELECT 'Clothing', 'Jeans', 80, 60
''')

# Calculate product ranking and cumulative sales by category
result = conn.execute('''
SELECT 
    category, 
    product, 
    price, 
    quantity,
    RANK() OVER (PARTITION BY category ORDER BY quantity DESC) as product_rank,
    SUM(quantity) OVER (PARTITION BY category ORDER BY price) as cumulative_category_sales
FROM product_sales
''').fetchall()

for row in result:
    print(row)