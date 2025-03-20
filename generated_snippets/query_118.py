# Generated: 2025-03-19 20:45:59.196203
# Result: [('Electronics', 'South', Decimal('145000.75')), ('Electronics', 'North', Decimal('125000.50')), ('Electronics', 'East', Decimal('92000.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create multi-dimensional sales table
conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product VARCHAR,
    total_sales DECIMAL(10,2),
    region VARCHAR
);
''')

# Insert sample sales data
conn.executemany('INSERT INTO product_sales VALUES (?, ?, ?, ?)', [
    ('Electronics', 'Laptop', 125000.50, 'North'),
    ('Electronics', 'Smartphone', 145000.75, 'South'),
    ('Electronics', 'Tablet', 92000.00, 'East')
])

# Perform multi-dimensional sales analysis
result = conn.execute('''
SELECT 
    category, 
    region, 
    SUM(total_sales) as total_sales
FROM product_sales
GROUP BY category, region
''').fetchall()

print(result)