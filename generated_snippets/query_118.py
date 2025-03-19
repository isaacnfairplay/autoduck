# Generated: 2025-03-19 09:51:04.865351
# Result: [('Electronics', 'Laptop', 1200), ('Electronics', 'Phone', 800)]
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
SELECT category, product_name, price
FROM products
WHERE category = 'Electronics'
""").fetchall()

print(result)