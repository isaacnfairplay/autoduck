# Generated: 2025-03-19 09:10:34.019656
# Result: [('Smartphone', 'Electronics', Decimal('799.99')), ('Laptop', 'Electronics', Decimal('1299.50'))]
# Valid: True
# Variable sales_data: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table using VALUES
sales_data = conn.execute('''
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200.50),
    ('Electronics', 'Phone', 800.25),
    ('Electronics', 'Tablet', 600.00)
) AS t(category, product, amount)
''').fetchall()

for row in sales_data:
    print(f'Category: {row[0]}, Product: {row[1]}, Amount: ${row[2]}')