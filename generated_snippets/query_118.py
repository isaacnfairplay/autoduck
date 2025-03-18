# Generated: 2025-03-18 05:46:14.673169
# Result: [('Electronics', 'Laptop', 1200, 1), ('Electronics', 'Smartphone', 800, 2), ('Clothing', 'Jeans', 100, 1), ('Clothing', 'Shirt', 50, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data
conn.sql("""
CREATE TABLE sales AS
SELECT 'Electronics' as category, 'Laptop' as product, 1200 as sale_amount
UNION ALL
SELECT 'Electronics', 'Smartphone', 800
UNION ALL
SELECT 'Clothing', 'Shirt', 50
UNION ALL
SELECT 'Clothing', 'Jeans', 100
""")

# Use window function to rank sales within categories
result = conn.sql("""
SELECT 
    category, 
    product, 
    sale_amount,
    RANK() OVER (PARTITION BY category ORDER BY sale_amount DESC) as sales_rank
FROM sales
""").fetchall()

for row in result:
    print(f"Category: {row[0]}, Product: {row[1]}, Amount: {row[2]}, Rank: {row[3]}")