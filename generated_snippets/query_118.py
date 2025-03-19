# Generated: 2025-03-19 08:03:54.252521
# Result: [('Electronics', 'Smartphone', Decimal('800.00'), Decimal('1300.00'), 1), ('Electronics', 'Laptop', Decimal('500.00'), Decimal('500.00'), 2), ('Clothing', 'Jeans', Decimal('100.00'), Decimal('150.00'), 1), ('Clothing', 'Shirt', Decimal('50.00'), Decimal('50.00'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data
conn.sql("""
CREATE TABLE product_sales AS
SELECT 'Electronics' as category, 'Laptop' as product, 500.00 as price UNION ALL
SELECT 'Electronics', 'Smartphone', 800.00 UNION ALL
SELECT 'Clothing', 'Shirt', 50.00 UNION ALL
SELECT 'Clothing', 'Jeans', 100.00
""")

# Calculate cumulative sales and rank products within category
result = conn.sql("""
SELECT 
    category, 
    product, 
    price,
    SUM(price) OVER (PARTITION BY category ORDER BY price) as cumulative_category_sales,
    RANK() OVER (PARTITION BY category ORDER BY price DESC) as product_rank
FROM product_sales
""").fetchall()

for row in result:
    print(row)