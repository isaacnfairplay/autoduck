# Generated: 2025-03-19 12:59:48.409785
# Result: [('Electronics', 'Laptop', 1200, 1), ('Electronics', 'Smartphone', 800, 2), ('Electronics', 'Headphones', 200, 3), ('Clothing', 'Pants', 75, 1), ('Clothing', 'Shirt', 50, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table
conn.execute('''
CREATE TABLE product_sales AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Smartphone', 800),
    ('Electronics', 'Headphones', 200),
    ('Clothing', 'Shirt', 50),
    ('Clothing', 'Pants', 75)
) AS t(category, product, sales);
''')

# Top products per category using window function
result = conn.execute('''
SELECT category, product, sales,
       RANK() OVER (PARTITION BY category ORDER BY sales DESC) as sales_rank
FROM product_sales
''').fetchall()

for row in result:
    print(row)