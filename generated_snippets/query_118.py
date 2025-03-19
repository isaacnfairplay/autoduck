# Generated: 2025-03-19 16:47:03.275014
# Result: [(2, datetime.date(2023, 5, 2), Decimal('275.25'), Decimal('275.25'), 1), (1, datetime.date(2023, 5, 1), Decimal('150.50'), Decimal('150.50'), 2), (1, datetime.date(2023, 5, 3), Decimal('89.99'), Decimal('240.49'), 3)]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create and populate customer order table
conn.execute('CREATE TABLE orders (customer_id INT, order_date DATE, total_amount DECIMAL(10,2))')
conn.executemany('INSERT INTO orders VALUES (?, ?, ?)', [
    (1, '2023-05-01', 150.50),
    (2, '2023-05-02', 275.25),
    (1, '2023-05-03', 89.99)
])

# Analyze orders using window functions
result = conn.execute('''
    SELECT 
        customer_id, 
        order_date, 
        total_amount,
        SUM(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date) as cumulative_spend,
        RANK() OVER (ORDER BY total_amount DESC) as order_rank
    FROM orders
''').fetchall()

print(result)