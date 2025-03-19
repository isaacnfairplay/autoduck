# Generated: 2025-03-19 09:01:00.431018
# Result: [('Electronics', 'Laptop', 1200, '2023-01-15', 1200), ('Electronics', 'Phone', 800, '2023-02-20', 2000), ('Electronics', 'Tablet', 500, '2023-05-12', 2500), ('Clothing', 'Shirt', 50, '2023-03-10', 50), ('Clothing', 'Jeans', 100, '2023-04-05', 150)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data with multiple columns
conn.sql("""
CREATE TABLE sales AS 
SELECT * FROM (
    VALUES
    ('Electronics', 'Laptop', 1200, '2023-01-15'),
    ('Electronics', 'Phone', 800, '2023-02-20'),
    ('Clothing', 'Shirt', 50, '2023-03-10'),
    ('Clothing', 'Jeans', 100, '2023-04-05'),
    ('Electronics', 'Tablet', 500, '2023-05-12')
) t(category, product, price, sale_date)
""")

# Demonstrate window function: running total by category
result = conn.sql("""
SELECT 
    category, 
    product, 
    price,
    sale_date,
    SUM(price) OVER (PARTITION BY category ORDER BY sale_date) as category_running_total
FROM sales
""").fetchall()

for row in result:
    print(row)

conn.close()
