# Generated: 2025-03-19 08:11:03.556346
# Result: [('Laptop', 'Electronics', 10, Decimal('1200.50')), ('Smartphone', 'Electronics', 15, Decimal('800.25')), ('Shoes', 'Clothing', 20, Decimal('150.00'))]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create sales table using CREATE TABLE AS with a derived query
conn.execute('''CREATE TABLE sales AS
SELECT
    'Laptop' as product,
    'Electronics' as category,
    10 as quantity,
    1200.50 as price
UNION ALL
SELECT
    'Smartphone' as product,
    'Electronics' as category,
    15 as quantity,
    800.25 as price
UNION ALL
SELECT
    'Shoes' as product,
    'Clothing' as category,
    20 as quantity,
    150.00 as price
''')

# Verify table creation
result = conn.execute('SELECT * FROM sales').fetchall()
for row in result:
    print(row)