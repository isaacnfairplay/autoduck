# Generated: 2025-03-19 20:44:16.890631
# Result: [('All', 'All', Decimal('362001.25')), ('Electronics', 'All', Decimal('362001.25')), ('Electronics', 'East', Decimal('92000.00')), ('Electronics', 'North', Decimal('125000.50')), ('Electronics', 'South', Decimal('145000.75'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a products table with sales tracking
conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product VARCHAR,
    total_sales DECIMAL(10,2),
    region VARCHAR
);
''')

# Insert sample multi-dimensional sales data
conn.executemany('INSERT INTO product_sales VALUES (?, ?, ?, ?)', [
    ('Electronics', 'Laptop', 125000.50, 'North'),
    ('Electronics', 'Smartphone', 145000.75, 'South'),
    ('Electronics', 'Tablet', 92000.00, 'East')
])

# Use advanced analytics with ROLLUP to get comprehensive sales summary
result = conn.execute('''
SELECT 
    COALESCE(category, 'All') as category,
    COALESCE(region, 'All') as region,
    SUM(total_sales) as total_sales
FROM product_sales
GROUP BY ROLLUP(category, region)
''').fetchall()

print(result)