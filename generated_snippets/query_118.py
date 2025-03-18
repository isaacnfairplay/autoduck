# Generated: 2025-03-18 17:50:26.619664
# Result: [('Electronics', Decimal('3001.00'), 12), ('Furniture', Decimal('1500.50'), 5)]
# Valid: True
import duckdb

con = duckdb.connect(':memory:')

# Create product sales tracking table
con.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    total_revenue DECIMAL(10,2),
    sales_volume INTEGER
);
''')

# Insert initial sales data
con.executemany('INSERT INTO product_sales VALUES (?, ?, ?)', [
    ('Electronics', 2250.75, 10),
    ('Furniture', 1500.50, 5),
    ('Electronics', 750.25, 2)
])

# Analyze aggregate sales performance
result = con.execute('''
SELECT 
    category, 
    SUM(total_revenue) as category_revenue,
    SUM(sales_volume) as total_volume
FROM product_sales
GROUP BY category
HAVING category_revenue > 1000
''').fetchall()

print(result)