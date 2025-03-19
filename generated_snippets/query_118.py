# Generated: 2025-03-19 12:52:50.894828
# Result: [('Headphones', 200, 200.0, 1), ('Laptop', 1200, 1200.0, 1), ('Smartphone', 800, 800.0, 1), ('Tablet', 500, 500.0, 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics sales table with new data
conn.execute('''
CREATE TABLE electronics_sales AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200, '2023-01-01'),
    ('Electronics', 'Smartphone', 800, '2023-02-01'),
    ('Electronics', 'Headphones', 200, '2023-03-01'),
    ('Electronics', 'Tablet', 500, '2023-01-03')
) AS t(category, product, price, sale_date);
''')

# Analyze sales performance with new product
result = conn.execute('''
SELECT 
    product, 
    SUM(price) as total_revenue,
    AVG(price) as average_price,
    COUNT(*) as sales_count
FROM electronics_sales
GROUP BY product
''').fetchall()

for row in result:
    print(row)