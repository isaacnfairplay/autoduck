# Generated: 2025-03-19 12:58:57.127691
# Result: [(1, 'Laptop', Decimal('1200.50')), (2, 'Smartphone', Decimal('800.25')), (3, 'Headphones', Decimal('150.75'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create simple products table
conn.execute('''
CREATE TABLE products AS SELECT * FROM (VALUES
    (1, 'Laptop', 1200.50),
    (2, 'Smartphone', 800.25),
    (3, 'Headphones', 150.75)
) AS t(id, name, price);
''')

# Perform simple SELECT * query
result = conn.execute('SELECT * FROM products').fetchall()

for row in result:
    print(row)