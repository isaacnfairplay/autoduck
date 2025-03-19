# Generated: 2025-03-19 12:53:42.152071
# Result: [('Pants', 75, 75.0, 1), ('Shirt', 50, 50.0, 1), ('Jacket', 120, 120.0, 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create clothing sales table with new product
conn.execute('''
CREATE TABLE clothing_sales AS
SELECT * FROM (VALUES
    ('Clothing', 'Shirt', 50, '2023-01-04'),
    ('Clothing', 'Pants', 75, '2023-02-01'),
    ('Clothing', 'Jacket', 120, '2023-03-15')
) AS t(category, product, price, sale_date);
''')

# Analyze clothing sales performance
result = conn.execute('''
SELECT 
    product, 
    SUM(price) as total_revenue,
    AVG(price) as average_price,
    COUNT(*) as sales_count
FROM clothing_sales
GROUP BY product
''').fetchall()

for row in result:
    print(row)