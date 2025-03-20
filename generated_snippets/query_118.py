# Generated: 2025-03-19 20:36:36.728185
# Result: [(1, 'Laptop', Decimal('1200.50')), (2, 'Smartphone', Decimal('800.75')), (3, 'Tablet', Decimal('500.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table from VALUES clause
result = conn.execute('''
SELECT * FROM (VALUES
    (1, 'Laptop', 1200.50),
    (2, 'Smartphone', 800.75),
    (3, 'Tablet', 500.00)
) AS products(id, name, price)
''').fetchall()

print(result)