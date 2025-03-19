# Generated: 2025-03-19 12:30:09.496385
# Result: [('Electronics', 'Laptop', Decimal('1200.00')), ('Furniture', 'Chair', Decimal('250.50'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create dynamic sales data from VALUES clause
result = conn.execute('''
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200.00),
    ('Clothing', 'Shirt', 50.00),
    ('Furniture', 'Chair', 250.50)
) AS t(category, product, amount)
WHERE amount > 100
''').fetchall()

for row in result:
    print(row)