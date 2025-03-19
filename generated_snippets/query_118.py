# Generated: 2025-03-19 09:39:05.815629
# Result: [('Phone', 800)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.sql("""
CREATE TABLE products AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Phone', 800),
    ('Clothing', 'T-Shirt', 50)
) t(category, product_name, price)
""")

result = conn.sql("""
SELECT product_name, price
FROM products
WHERE category = 'Electronics' AND product_name = 'Phone'
""").fetchall()

print(result)