# Generated: 2025-03-19 09:42:29.243652
# Result: [('Electronics', 'Phone', 750), ('Books', 'Textbook', 600)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.sql("""
CREATE TABLE sales AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 500),
    ('Electronics', 'Phone', 750),
    ('Clothing', 'Shirt', 300),
    ('Clothing', 'Pants', 450),
    ('Books', 'Novel', 200),
    ('Books', 'Textbook', 600)
) t(category, product, amount)
""")

result = conn.sql("""
SELECT category, product, amount
FROM sales
WHERE amount > 500
""").fetchall()

print(result)