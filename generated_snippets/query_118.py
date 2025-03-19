# Generated: 2025-03-19 09:04:34.003032
# Result: [('South', 'Laptop', Decimal('1500.75'), 1), ('West', 'Laptop', Decimal('2150.80'), 2), ('West', 'Phone', Decimal('2150.80'), 3), ('East', 'Phone', Decimal('800.25'), 4), ('Midwest', 'Tablet', Decimal('600.00'), 5)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with geographic dimension
conn.execute('CREATE TABLE regional_sales (region TEXT, product TEXT, sale_amount DECIMAL(10,2), sale_date DATE)')

# Insert diverse sales data with multiple dimensions
conn.executemany('INSERT INTO regional_sales VALUES (?, ?, ?, ?)', [
    ('West', 'Laptop', 1200.50, '2023-05-15'),
    ('East', 'Phone', 800.25, '2023-05-16'),
    ('Midwest', 'Tablet', 600.00, '2023-05-17'),
    ('South', 'Laptop', 1500.75, '2023-05-18'),
    ('West', 'Phone', 950.30, '2023-05-19')
])

# Analyze sales with advanced window and aggregation functions
result = conn.execute('''SELECT
    region,
    product,
    SUM(sale_amount) OVER (PARTITION BY region) as regional_total,
    RANK() OVER (ORDER BY sale_amount DESC) as sale_rank
FROM regional_sales
''').fetchall()

for row in result:
    print(f"Region: {row[0]}, Product: {row[1]}, Regional Total: ${row[2]}, Sale Rank: {row[3]}")