# Generated: 2025-03-19 13:49:27.886761
# Result: [('South', 'Smartphone', Decimal('7500.75'), 1), ('West', 'Laptop', Decimal('6100.00'), 1), ('North', 'Laptop', Decimal('5000.50'), 1), ('North', 'Smartphone', Decimal('4800.90'), 2), ('East', 'Tablet', Decimal('3200.25'), 1)]
# Valid: True
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create table with geographic sales data
conn.execute('''
CREATE TABLE sales (
    region VARCHAR,
    product VARCHAR,
    revenue DECIMAL(10,2)
)''')

# Insert sample sales data
conn.execute('''
INSERT INTO sales VALUES
    ('North', 'Laptop', 5000.50),
    ('South', 'Smartphone', 7500.75),
    ('East', 'Tablet', 3200.25),
    ('West', 'Laptop', 6100.00),
    ('North', 'Smartphone', 4800.90)
''')

# Perform window function to rank products by revenue within each region
result = conn.execute('''
SELECT 
    region, 
    product, 
    revenue,
    RANK() OVER (PARTITION BY region ORDER BY revenue DESC) as revenue_rank
FROM sales
''').fetchall()

print(result)