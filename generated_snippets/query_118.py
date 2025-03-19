# Generated: 2025-03-19 09:39:56.924185
# Result: [('Tablet', 500)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.sql("""
CREATE TABLE products AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Phone', 800),
    ('Electronics', 'Tablet', 500),
    ('Clothing', 'T-Shirt', 50)
) t(category, product_name, price)
""")

result = conn.sql("""
SELECT product_name, price
FROM products
WHERE category = 'Electronics' AND product_name = 'Tablet'
""").fetchall()

print(result)