# Generated: 2025-03-19 09:08:00.658907
# Result: [('Electronics', 'Laptop', Decimal('1200.00')), ('Electronics', 'Phone', Decimal('800.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics sales table
conn.execute('CREATE TABLE electronics_sales (category TEXT, product TEXT, sale_price DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO electronics_sales VALUES (?, ?, ?)', [
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Phone', 800),
    ('Electronics', 'Tablet', 600)
])

# Query to show electronics sales with filtering
result = conn.execute(
    'SELECT category, product, sale_price FROM electronics_sales WHERE sale_price > 700'
).fetchall()

for row in result:
    print(f'Category: {row[0]}, Product: {row[1]}, Price: ${row[2]}')