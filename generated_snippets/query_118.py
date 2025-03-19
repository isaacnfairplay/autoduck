# Generated: 2025-03-19 09:41:38.734856
# Result: [('Pants', 100)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.sql("""
CREATE TABLE products AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200),
    ('Clothing', 'Shirt', 50),
    ('Clothing', 'Pants', 100)
) t(category, product_name, price)
""")

result = conn.sql("""
SELECT product_name, price
FROM products
WHERE category = 'Clothing' AND product_name = 'Pants'
""").fetchall()

print(result)