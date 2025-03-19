# Generated: 2025-03-19 08:55:45.306356
# Result: [('Electronics', Decimal('500.25'), Decimal('500.25')), ('Electronics', Decimal('1000.50'), Decimal('1500.75')), ('Clothing', Decimal('600.30'), Decimal('600.30')), ('Clothing', Decimal('750.75'), Decimal('1351.05'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate sales table
conn.execute('CREATE TABLE category_sales (category TEXT, amount DECIMAL(10,2))')
conn.executemany('INSERT INTO category_sales VALUES (?, ?)', [
    ('Electronics', 1000.50),
    ('Electronics', 500.25), 
    ('Clothing', 750.75),
    ('Clothing', 600.30)
])

# Calculate running total per category using window function
result = conn.execute('''
    SELECT 
        category, 
        amount, 
        SUM(amount) OVER (PARTITION BY category ORDER BY amount) as running_total
    FROM category_sales
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Amount: ${row[1]}, Running Total: ${row[2]:.2f}")