# Generated: 2025-03-19 16:47:54.994726
# Result: [('West', 'Laptop', Decimal('6200.00'), 1, 1), ('North', 'Laptop', Decimal('5000.50'), 1, 2), ('East', 'Phone', Decimal('4500.25'), 1, 3), ('South', 'Tablet', Decimal('3200.75'), 1, 4)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create geographical sales data
conn.execute('CREATE TABLE regional_sales (region VARCHAR, product VARCHAR, sales_amount DECIMAL(10,2))')
conn.executemany('INSERT INTO regional_sales VALUES (?, ?, ?)', [
    ('North', 'Laptop', 5000.50),
    ('South', 'Tablet', 3200.75),
    ('East', 'Phone', 4500.25),
    ('West', 'Laptop', 6200.00)
])

# Use window function and ranking to analyze regional sales performance
result = conn.execute('''
    SELECT 
        region, 
        product, 
        sales_amount,
        RANK() OVER (PARTITION BY region ORDER BY sales_amount DESC) as regional_rank,
        DENSE_RANK() OVER (ORDER BY sales_amount DESC) as overall_rank
    FROM regional_sales
''').fetchall()

print(result)