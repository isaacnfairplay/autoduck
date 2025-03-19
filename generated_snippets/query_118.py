# Generated: 2025-03-19 12:51:08.039672
# Result: [('Headphones', 200, 200.0), ('Laptop', 1200, 1200.0), ('Smartphone', 800, 800.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics sales table
conn.execute('''
CREATE TABLE electronics_sales AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200, '2023-01-01'),
    ('Electronics', 'Smartphone', 800, '2023-02-01'),
    ('Electronics', 'Headphones', 200, '2023-03-01')
) AS t(category, product, price, sale_date);
''')

# Query to analyze electronics sales
result = conn.execute('''
SELECT 
    product, 
    SUM(price) as total_revenue,
    AVG(price) as avg_price
FROM electronics_sales
GROUP BY product
''').fetchall()

for row in result:
    print(row)