# Generated: 2025-03-19 10:34:02.039431
# Result: [('Tablet', Decimal('500.75'), datetime.date(2023, 1, 17), 500.75, Decimal('500.75')), ('Laptop', Decimal('1200.50'), datetime.date(2023, 1, 15), 1250.25, Decimal('1200.50')), ('Laptop', Decimal('1300.00'), datetime.date(2023, 1, 18), 1250.25, Decimal('1200.50')), ('Phone', Decimal('800.25'), datetime.date(2023, 1, 16), 775.425, Decimal('800.25')), ('Phone', Decimal('750.60'), datetime.date(2023, 1, 19), 775.425, Decimal('800.25'))]
# Valid: True
import duckdb

# Complex window function with offset and frame specification
conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE sales (product TEXT, amount DECIMAL(10,2), sale_date DATE)')
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('Laptop', 1200.50, '2023-01-15'),
    ('Phone', 800.25, '2023-01-16'),
    ('Tablet', 500.75, '2023-01-17'),
    ('Laptop', 1300.00, '2023-01-18'),
    ('Phone', 750.60, '2023-01-19')
])

result = conn.execute('''
    SELECT 
        product, 
        amount, 
        sale_date,
        AVG(amount) OVER (
            PARTITION BY product 
            ORDER BY sale_date 
            ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
        ) as rolling_avg,
        FIRST_VALUE(amount) OVER (
            PARTITION BY product 
            ORDER BY sale_date
        ) as first_product_sale
    FROM sales
''').fetchall()

for row in result:
    print(row)