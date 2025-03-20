# Generated: 2025-03-19 21:28:46.787138
# Result: [('North', 'Laptop', Decimal('5000.50'), Decimal('5000.50')), ('North', 'Desktop', Decimal('7500.25'), Decimal('12500.75')), ('South', 'Tablet', Decimal('3200.75'), Decimal('3200.75')), ('West', 'Tablet', Decimal('2900.60'), Decimal('2900.60')), ('East', 'Laptop', Decimal('4800.00'), Decimal('4800.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with geographical sales data
conn.execute('''CREATE TABLE sales (
    region VARCHAR,
    product VARCHAR,
    revenue DECIMAL(10,2)
)''')

# Insert sample sales data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('North', 'Laptop', 5000.50),
    ('South', 'Tablet', 3200.75),
    ('North', 'Desktop', 7500.25),
    ('East', 'Laptop', 4800.00),
    ('West', 'Tablet', 2900.60)
])

# Perform window function to calculate running total by region
result = conn.sql('''
    SELECT 
        region, 
        product, 
        revenue,
        SUM(revenue) OVER (PARTITION BY region ORDER BY revenue) as running_total
    FROM sales
''').fetchall()

print(result)