# Generated: 2025-03-19 12:57:13.307314
# Result: [('Electronics', 'Laptop', 1200, 1), ('Electronics', 'Smartphone', 800, 2), ('Clothing', 'Jacket', 120, 1), ('Clothing', 'Pants', 75, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales data
conn.execute('''
CREATE TABLE product_sales AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Smartphone', 800),
    ('Electronics', 'Headphones', 200),
    ('Electronics', 'Tablet', 500),
    ('Clothing', 'Shirt', 50),
    ('Clothing', 'Pants', 75),
    ('Clothing', 'Jacket', 120)
) AS t(category, product, sales);
''')

# Use QUALIFY to get top 2 products per category
result = conn.execute('''
SELECT category, product, sales,
       RANK() OVER (PARTITION BY category ORDER BY sales DESC) as sales_rank
FROM product_sales
QUALIFY sales_rank <= 2
''').fetchall()

for row in result:
    print(row)