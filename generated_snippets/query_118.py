# Generated: 2025-03-19 09:17:41.695596
# Result: [('Electronics', Decimal('800.75'), Decimal('800.75')), ('Electronics', Decimal('1200.50'), Decimal('2001.25')), ('Clothing', Decimal('350.00'), Decimal('350.00')), ('Clothing', Decimal('500.25'), Decimal('850.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table
conn.execute('CREATE TABLE sales (category TEXT, amount DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO sales VALUES (?, ?)', [
    ('Electronics', 1200.50),
    ('Clothing', 500.25),
    ('Electronics', 800.75),
    ('Clothing', 350.00)
])

# Calculate running total per category using window function
result = conn.execute('''SELECT
    category,
    amount,
    SUM(amount) OVER (PARTITION BY category ORDER BY amount) as running_total
FROM sales
''').fetchall()

for row in result:
    print(f'Category: {row[0]}, Amount: ${row[1]}, Running Total: ${row[2]}')