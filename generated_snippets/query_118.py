# Generated: 2025-03-19 09:40:47.374128
# Result: [('Shirt', 50)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.sql("""
CREATE TABLE products AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200),
    ('Clothing', 'Shirt', 50)
) t(category, product_name, price)
""")

result = conn.sql("""
SELECT product_name, price
FROM products
WHERE category = 'Clothing' AND product_name = 'Shirt'
""").fetchall()

print(result)