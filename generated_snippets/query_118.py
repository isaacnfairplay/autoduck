# Generated: 2025-03-19 14:21:47.490241
# Result: [('South', 'Laptop', Decimal('4500.25'), 1), ('South', 'Phone', Decimal('2800.60'), 2), ('North', 'Laptop', Decimal('5000.50'), 1), ('North', 'Phone', Decimal('3200.75'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with geographic sales data
conn.execute('CREATE TABLE regional_sales (region STRING, product STRING, sales DECIMAL(10,2))')
conn.execute("""INSERT INTO regional_sales VALUES
    ('North', 'Laptop', 5000.50),
    ('North', 'Phone', 3200.75),
    ('South', 'Laptop', 4500.25),
    ('South', 'Phone', 2800.60)
""")

# Use window functions to rank products within each region
result = conn.execute('''
    SELECT 
        region, 
        product, 
        sales,
        RANK() OVER (PARTITION BY region ORDER BY sales DESC) as sales_rank
    FROM regional_sales
''').fetchall()

for row in result:
    print(row)