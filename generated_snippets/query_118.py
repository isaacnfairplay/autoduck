# Generated: 2025-03-19 20:41:40.524332
# Result: [('Electronics', 'Laptop', Decimal('1200.50')), ('Electronics', 'Smartphone', Decimal('800.75'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create dynamic table from VALUES clause
result = conn.execute('''
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200.50),
    ('Electronics', 'Smartphone', 800.75),
    ('Clothing', 'Shirt', 50.00)
) AS t(category, product, amount)
WHERE category = 'Electronics'
''').fetchall()

print(result)