# Generated: 2025-03-19 19:32:33.922758
# Result: [('Phone', 7500, 1), ('Laptop', 5000, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample product sales data
conn.execute('''
CREATE TABLE product_sales AS
SELECT 'Laptop' as product, 5000 as sales
UNION ALL
SELECT 'Phone', 7500
UNION ALL
SELECT 'Tablet', 3200
UNION ALL
SELECT 'Smartwatch', 2800
''')

# Use QUALIFY to get top 2 products by sales with window function
result = conn.execute('''
SELECT product, sales,
       RANK() OVER (ORDER BY sales DESC) as sales_rank
FROM product_sales
QUALIFY sales_rank <= 2
''').fetchall()

print(result)