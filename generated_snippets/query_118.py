# Generated: 2025-03-19 10:41:49.442946
# Result: [('Laptop', Decimal('1200.50')), ('Phone', Decimal('800.25')), ('Tablet', Decimal('500.75')), ('Camera', Decimal('1100.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create first sales table
conn.execute('CREATE TABLE sales_2022 (product TEXT, amount DECIMAL(10,2))')
conn.executemany('INSERT INTO sales_2022 VALUES (?, ?)', [
    ('Laptop', 1200.50),
    ('Phone', 800.25)
])

# Create second sales table
conn.execute('CREATE TABLE sales_2023 (product TEXT, amount DECIMAL(10,2))')
conn.executemany('INSERT INTO sales_2023 VALUES (?, ?)', [
    ('Tablet', 500.75),
    ('Camera', 1100.00)
])

# Use UNION ALL to combine results
result = conn.execute('''
    SELECT product, amount FROM sales_2022
    UNION ALL
    SELECT product, amount FROM sales_2023
''').fetchall()

for row in result:
    print(row)