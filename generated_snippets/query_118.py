# Generated: 2025-03-19 20:49:23.616390
# Result: [(102, datetime.date(2023, 6, 16), Decimal('150.50'), Decimal('150.50')), (101, datetime.date(2023, 6, 15), Decimal('250.75'), Decimal('250.75')), (101, datetime.date(2023, 6, 17), Decimal('350.25'), Decimal('601.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample table for customer orders
conn.execute('''
CREATE TABLE orders (
    order_id INTEGER,
    customer_id INTEGER,
    total_amount DECIMAL(10,2),
    order_date DATE
);
''')

# Insert sample order data
conn.executemany('INSERT INTO orders VALUES (?, ?, ?, ?)', [
    (1, 101, 250.75, '2023-06-15'),
    (2, 102, 150.50, '2023-06-16'),
    (3, 101, 350.25, '2023-06-17')
])

# Perform aggregation with window function
result = conn.execute('''
SELECT 
    customer_id, 
    order_date, 
    total_amount,
    SUM(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date) as cumulative_spend
FROM orders
''').fetchall()

print(result)