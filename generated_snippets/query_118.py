# Generated: 2025-03-19 09:15:04.973770
# Result: [('West', 'Laptop', datetime.date(2023, 8, 1), Decimal('1200.50'), 1, Decimal('1200.50')), ('East', 'Phone', datetime.date(2023, 8, 2), Decimal('800.25'), 1, Decimal('800.25')), ('Midwest', 'Tablet', datetime.date(2023, 8, 3), Decimal('600.00'), 1, Decimal('600.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales tracking with multiple dimensions
conn.execute('CREATE TABLE advanced_sales (region TEXT, product TEXT, sale_date DATE, amount DECIMAL(10,2))')

conn.executemany('INSERT INTO advanced_sales VALUES (?, ?, ?, ?)', [
    ('West', 'Laptop', '2023-08-01', 1200.50),
    ('East', 'Phone', '2023-08-02', 800.25),
    ('Midwest', 'Tablet', '2023-08-03', 600.00)
])

# Demonstrate complex multi-dimensional analysis with window functions
result = conn.execute('''SELECT
    region,
    product,
    sale_date,
    amount,
    RANK() OVER (PARTITION BY region ORDER BY amount DESC) as regional_rank,
    SUM(amount) OVER (PARTITION BY region) as regional_total
FROM advanced_sales
''').fetchall()

for row in result:
    print(f'Region: {row[0]}, Product: {row[1]}, Date: {row[2]}, Amount: ${row[3]}, Regional Rank: {row[4]}, Regional Total: ${row[5]}')