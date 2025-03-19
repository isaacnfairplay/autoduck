# Generated: 2025-03-19 09:15:57.149399
# Result: [('Phone', 500, Decimal('800.25'), Decimal('400125.00'), 1), ('Laptop', 250, Decimal('1200.50'), Decimal('300125.00'), 2), ('Tablet', 150, Decimal('600.00'), Decimal('90000.00'), 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales tracking table
conn.execute('CREATE TABLE product_performance (product TEXT, sales_volume INT, unit_price DECIMAL(10,2))')

# Insert sample product data
conn.executemany('INSERT INTO product_performance VALUES (?, ?, ?)', [
    ('Laptop', 250, 1200.50),
    ('Phone', 500, 800.25),
    ('Tablet', 150, 600.00)
])

# Analyze product performance with advanced window functions
result = conn.execute('''SELECT
    product,
    sales_volume,
    unit_price,
    sales_volume * unit_price as total_revenue,
    RANK() OVER (ORDER BY sales_volume * unit_price DESC) as revenue_rank
FROM product_performance
''').fetchall()

for row in result:
    print(f'Product: {row[0]}, Sales Volume: {row[1]}, Unit Price: ${row[2]}, Total Revenue: ${row[3]}, Revenue Rank: {row[4]}')