# Generated: 2025-03-19 09:06:19.482671
# Result: [('Laptop', '2023-07-15', Decimal('1200.50')), ('Phone', '2023-07-16', Decimal('800.25')), ('Tablet', '2023-07-17', Decimal('600.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table using CREATE TABLE AS (CTAS)
conn.execute('''
CREATE TABLE sales AS
SELECT * FROM (
    VALUES
    ('Laptop', '2023-07-15', 1200.50),
    ('Phone', '2023-07-16', 800.25),
    ('Tablet', '2023-07-17', 600.00)
) AS t(product, sale_date, amount)
''')

# Verify table creation
result = conn.execute('SELECT * FROM sales').fetchall()
for row in result:
    print(row)