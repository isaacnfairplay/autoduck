# Generated: 2025-03-19 12:50:16.204209
# Result: [(1, 'Laptop', Decimal('1200.50')), (2, 'Smartphone', Decimal('800.25')), (3, 'Headphones', Decimal('150.75'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales data using VALUES clause
result = conn.execute('''
SELECT * FROM (VALUES
    (1, 'Laptop', 1200.50),
    (2, 'Smartphone', 800.25),
    (3, 'Headphones', 150.75)
) AS products(id, name, price)
''').fetchall()

for row in result:
    print(row)