# Generated: 2025-03-19 09:38:14.461933
# Result: [('Laptop', 1200), ('Smartphone', 800)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create products table with tuple data
conn.sql("""
CREATE TABLE products AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Smartphone', 800),
    ('Clothing', 'T-Shirt', 50)
) t(category, product_name, price)
""")

# Query to filter products by category
result = conn.sql("""
SELECT product_name, price
FROM products
WHERE category = 'Electronics'
""").fetchall()

print(result)