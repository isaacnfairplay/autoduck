# Generated: 2025-03-19 12:54:34.282840
# Result: [('Pants', 175, 87.5, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE clothing_sales AS
SELECT * FROM (VALUES
    ('Clothing', 'Shirt', 50, '2023-01-04'),
    ('Clothing', 'Pants', 75, '2023-02-01'),
    ('Clothing', 'Jacket', 120, '2023-03-15'),
    ('Clothing', 'Pants', 100, '2023-01-05')
) AS t(category, product, price, sale_date);
''')

result = conn.execute('''
SELECT 
    product, 
    SUM(price) as total_revenue,
    AVG(price) as average_price,
    COUNT(*) as sales_count
FROM clothing_sales
WHERE product = 'Pants'
GROUP BY product
''').fetchall()

for row in result:
    print(row)