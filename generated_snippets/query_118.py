# Generated: 2025-03-19 13:00:40.022692
# Result: [('Electronics', 'Laptop', 1200), ('Electronics', 'Smartphone', 800), ('Clothing', 'Pants', 75), ('Clothing', 'Shirt', 50)]
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
) AS t(category, product, amount);
''')

# Use ROW_NUMBER() with QUALIFY to get top 2 products per category
result = conn.execute('''
SELECT category, product, amount
FROM product_sales
QUALIFY ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC) <= 2
''').fetchall()

for row in result:
    print(row)