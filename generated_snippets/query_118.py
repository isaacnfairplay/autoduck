# Generated: 2025-03-19 11:30:14.212138
# Result: [('Laptop', 'Electronics', Decimal('1500.00'), '2023-01-15'), ('Smartphone', 'Electronics', Decimal('850.50'), '2023-02-20'), ('Running Shoes', 'Sports', Decimal('120.00'), '2023-03-10'), ('Headphones', 'Electronics', Decimal('199.99'), '2023-01-25')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with various attributes
conn.execute('''
CREATE TABLE sales AS
SELECT 'Laptop' as product, 'Electronics' as category, 1500.00 as price, '2023-01-15' as sale_date
UNION ALL
SELECT 'Smartphone', 'Electronics', 850.50, '2023-02-20'
UNION ALL
SELECT 'Running Shoes', 'Sports', 120.00, '2023-03-10'
UNION ALL
SELECT 'Headphones', 'Electronics', 199.99, '2023-01-25'
''')

# Verify table creation
result = conn.execute('SELECT * FROM sales').fetchall()
for row in result:
    print(row)