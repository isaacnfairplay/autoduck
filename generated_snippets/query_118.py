# Generated: 2025-03-19 09:01:58.194117
# Result: [('Laptop', datetime.date(2023, 1, 15), Decimal('1200.50'), Decimal('1200.50')), ('Laptop', datetime.date(2023, 1, 17), Decimal('1500.75'), Decimal('2701.25')), ('Phone', datetime.date(2023, 1, 16), Decimal('800.25'), Decimal('800.25')), ('Phone', datetime.date(2023, 1, 19), Decimal('950.30'), Decimal('1750.55')), ('Tablet', datetime.date(2023, 1, 18), Decimal('600.00'), Decimal('600.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample sales dataset
conn.execute('''
    CREATE TABLE sales (product TEXT, sale_date DATE, amount DECIMAL(10,2))
''')

conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('Laptop', '2023-01-15', 1200.50),
    ('Phone', '2023-01-16', 800.25),
    ('Laptop', '2023-01-17', 1500.75),
    ('Tablet', '2023-01-18', 600.00),
    ('Phone', '2023-01-19', 950.30)
])

# Use window function to calculate rolling cumulative sales per product
result = conn.execute('''
    SELECT 
        product, 
        sale_date, 
        amount,
        SUM(amount) OVER (PARTITION BY product ORDER BY sale_date) as cumulative_sales
    FROM sales
    ORDER BY product, sale_date
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Date: {row[1]}, Sale: ${row[2]}, Cumulative Sales: ${row[3]}")