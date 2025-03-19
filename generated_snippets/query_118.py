# Generated: 2025-03-19 08:38:32.242908
# Result: [('South', 'Laptop', Decimal('4800.60'), 0, 0), ('North', None, Decimal('9500.75'), 0, 1), ('South', None, Decimal('8001.35'), 0, 1), ('North', 'Laptop', Decimal('5000.50'), 0, 0), ('North', 'Desktop', Decimal('4500.25'), 0, 0), ('South', 'Tablet', Decimal('3200.75'), 0, 0), (None, 'Laptop', Decimal('9801.10'), 1, 0), (None, 'Desktop', Decimal('4500.25'), 1, 0), (None, None, Decimal('17502.10'), 1, 1), (None, 'Tablet', Decimal('3200.75'), 1, 0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with geographic sales data
conn.execute('CREATE TABLE sales (region TEXT, product TEXT, revenue DECIMAL(10,2))')
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('North', 'Laptop', 5000.50), 
    ('South', 'Tablet', 3200.75),
    ('North', 'Desktop', 4500.25),
    ('South', 'Laptop', 4800.60)
])

# Perform multi-dimensional aggregation with GROUPING SETS
result = conn.execute('''
    SELECT 
        region, 
        product, 
        SUM(revenue) as total_revenue,
        GROUPING(region) as region_grouping,
        GROUPING(product) as product_grouping
    FROM sales
    GROUP BY GROUPING SETS ((region, product), (region), (product), ())
''').fetchall()

for row in result:
    print(f"Region: {row[0]}, Product: {row[1]}, Revenue: {row[2]}, Region Grouping: {row[3]}, Product Grouping: {row[4]}")