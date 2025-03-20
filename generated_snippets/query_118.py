# Generated: 2025-03-19 20:33:11.005222
# Result: [('South', 'All', Decimal('177000.25')), ('All', 'All', Decimal('447001.50')), ('North', 'Laptop', Decimal('270001.25')), ('North', 'All', Decimal('270001.25')), ('South', 'Tablet', Decimal('177000.25')), ('All', 'Laptop', Decimal('270001.25')), ('All', 'Tablet', Decimal('177000.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with multidimensional data
conn.execute('''
CREATE TABLE product_sales (
    region VARCHAR,
    product VARCHAR,
    quarter INTEGER,
    year INTEGER,
    total_sales DECIMAL(10,2)
);''')

# Insert sample multidimensional sales data
conn.executemany('INSERT INTO product_sales VALUES (?, ?, ?, ?, ?)', [
    ('North', 'Laptop', 1, 2023, 125000.50),
    ('North', 'Laptop', 2, 2023, 145000.75),
    ('South', 'Tablet', 1, 2023, 85000.25),
    ('South', 'Tablet', 2, 2023, 92000.00)
])

# Analyze sales with CUBE for comprehensive aggregation
result = conn.execute('''
SELECT 
    COALESCE(region, 'All') as region,
    COALESCE(product, 'All') as product,
    SUM(total_sales) as total_sales
FROM product_sales
GROUP BY CUBE(region, product)
''').fetchall()

print(result)