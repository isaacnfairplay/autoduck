# Generated: 2025-03-19 12:51:59.446380
# Result: [('Smartphone', 800, 1), ('Phone', 800, 1), ('Laptop', 1200, 1), ('Headphones', 200, 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create updated electronics sales table
conn.execute('''
CREATE TABLE electronics_sales AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200, '2023-01-01'),
    ('Electronics', 'Smartphone', 800, '2023-02-01'),
    ('Electronics', 'Headphones', 200, '2023-03-01'),
    ('Electronics', 'Phone', 800, '2023-01-02')
) AS t(category, product, price, sale_date);
''')

# Analyze sales with new product
result = conn.execute('''
SELECT 
    product, 
    SUM(price) as total_revenue,
    COUNT(*) as sales_count
FROM electronics_sales
GROUP BY product
''').fetchall()

for row in result:
    print(row)