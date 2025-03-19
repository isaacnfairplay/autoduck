# Generated: 2025-03-19 09:44:12.054283
# Result: [('Books', 'Textbook', 600, 1), ('Books', 'Novel', 200, 2), ('Electronics', 'Phone', 750, 1), ('Electronics', 'Laptop', 500, 2), ('Clothing', 'Pants', 450, 1), ('Clothing', 'Shirt', 300, 2)]
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
SELECT
    category,
    product,
    amount,
    RANK() OVER (PARTITION BY category ORDER BY amount DESC) as sales_rank
FROM sales
""").fetchall()

print(result)