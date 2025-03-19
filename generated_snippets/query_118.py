# Generated: 2025-03-19 19:58:26.747125
# Result: [('Tablet', datetime.date(2023, 1, 18), Decimal('500.00'), Decimal('500.00')), ('Laptop', datetime.date(2023, 1, 15), Decimal('1200.50'), Decimal('1200.50')), ('Laptop', datetime.date(2023, 1, 17), Decimal('1100.75'), Decimal('2301.25')), ('Phone', datetime.date(2023, 1, 16), Decimal('800.25'), Decimal('800.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample data for window function demo
conn.execute('CREATE TABLE sales (product TEXT, sale_date DATE, amount DECIMAL(10,2))')
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ['Laptop', '2023-01-15', 1200.50],
    ['Phone', '2023-01-16', 800.25],
    ['Laptop', '2023-01-17', 1100.75],
    ['Tablet', '2023-01-18', 500.00]
])

# Demonstrate cumulative sum window function
result = conn.execute('''
    SELECT 
        product, 
        sale_date, 
        amount, 
        SUM(amount) OVER (PARTITION BY product ORDER BY sale_date) as cumulative_product_sales
    FROM sales
''').fetchall()

for row in result:
    print(row)