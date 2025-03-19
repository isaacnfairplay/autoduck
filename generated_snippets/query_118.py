# Generated: 2025-03-19 08:34:07.170212
# Result: [('Electronics', 'Smartphone', 800, 75, 1, 75), ('Electronics', 'Laptop', 1200, 50, 2, 125), ('Clothing', 'Shirt', 50, 100, 1, 100), ('Clothing', 'Jeans', 80, 60, 2, 160)]
# Valid: True
# Variable results: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data with timestamps
conn.sql("""
CREATE TABLE sales AS
SELECT * FROM (
    VALUES
    ('2023-01-15', 'Product A', 100),
    ('2023-01-16', 'Product B', 150),
    ('2023-01-17', 'Product A', 200),
    ('2023-01-18', 'Product C', 250)
) t(sale_date, product, amount)
""")

# Demonstrate cumulative sum window function
results = conn.sql("""
SELECT 
    sale_date, 
    product, 
    amount,
    SUM(amount) OVER (PARTITION BY product ORDER BY sale_date) as cumulative_product_sales
FROM sales
""").fetchall()

for row in results:
    print(row)