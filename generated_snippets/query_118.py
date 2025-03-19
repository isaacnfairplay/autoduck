# Generated: 2025-03-19 08:17:01.767743
# Result: [('Electronics', 'Tablet', Decimal('500.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE product_sales AS
SELECT * FROM (VALUES
    ('Electronics', 'Tablet', 500.00)
) AS t(category, product, sale_amount)
''')

result = conn.execute('SELECT * FROM product_sales').fetchall()
for row in result:
    print(row)