# Generated: 2025-03-19 15:04:49.611541
# Result: [('phone', 25, Decimal('599.50'), Decimal('21741.25'), 1), ('laptop', 10, Decimal('999.99'), Decimal('31741.15'), 2), ('tablet', 15, Decimal('450.25'), Decimal('6753.75'), 3)]
# Valid: True
import duckdb

# Create an in-memory database and table with sales data
conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE sales (product TEXT, quantity INTEGER, price DECIMAL(10,2))')
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('laptop', 10, 999.99),
    ('phone', 25, 599.50),
    ('tablet', 15, 450.25)
])

# Use window function to calculate running total and rank products by sales
result = conn.execute('''
    SELECT 
        product, 
        quantity, 
        price, 
        SUM(quantity * price) OVER (ORDER BY price) as running_total,
        RANK() OVER (ORDER BY quantity * price DESC) as sales_rank
    FROM sales
''').fetchall()

for row in result:
    print(f'Product: {row[0]}, Rank: {row[4]}, Running Total: ${row[3]:.2f}')