# Generated: 2025-03-19 19:48:55.147495
# Result: [('Electronics', 2700, 2), ('Clothing', 1750, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create inline table with categorical aggregation
result = conn.execute('''
WITH sales_data(category, product, amount) AS (
    VALUES
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Phone', 1500),
    ('Clothing', 'Shirt', 800),
    ('Clothing', 'Pants', 950)
)
SELECT 
    category, 
    SUM(amount) as total_category_sales,
    COUNT(DISTINCT product) as unique_products
FROM sales_data
GROUP BY category
ORDER BY total_category_sales DESC
''').fetchall()

print(result)