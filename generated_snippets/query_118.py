# Generated: 2025-03-19 09:12:18.470476
# Result: [('Electronics', datetime.date(2023, 7, 15), Decimal('1200.50'), Decimal('1200.50')), ('Electronics', datetime.date(2023, 7, 17), Decimal('800.75'), Decimal('2001.25')), ('Clothing', datetime.date(2023, 7, 16), Decimal('500.25'), Decimal('500.25')), ('Clothing', datetime.date(2023, 7, 18), Decimal('350.00'), Decimal('850.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table
conn.execute('CREATE TABLE sales (category TEXT, amount DECIMAL(10,2), sale_date DATE)')

# Insert sample data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('Electronics', 1200.50, '2023-07-15'),
    ('Clothing', 500.25, '2023-07-16'),
    ('Electronics', 800.75, '2023-07-17'),
    ('Clothing', 350.00, '2023-07-18')
])

# Calculate running total per category
result = conn.execute('''SELECT
    category,
    sale_date,
    amount,
    SUM(amount) OVER (PARTITION BY category ORDER BY sale_date) as running_total
FROM sales
''').fetchall()

for row in result:
    print(f'Category: {row[0]}, Date: {row[1]}, Amount: ${row[2]}, Running Total: ${row[3]}')