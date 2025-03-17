# Generated: 2025-03-16 22:39:54.635092
# Result: [(1, datetime.date(2023, 1, 15), Decimal('250.50'), Decimal('250.50')), (1, datetime.date(2023, 2, 20), Decimal('175.25'), Decimal('425.75')), (2, datetime.date(2023, 1, 10), Decimal('300.75'), Decimal('300.75')), (2, datetime.date(2023, 3, 5), Decimal('225.00'), Decimal('525.75'))]
# Valid: True
import duckdb

# Establish an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample table for customer orders
conn.execute('''
CREATE TABLE customer_orders (
    customer_id INTEGER,
    order_date DATE,
    total_amount DECIMAL(10,2)
)''')

# Insert sample data
conn.executemany('INSERT INTO customer_orders VALUES (?, ?, ?)', [
    (1, '2023-01-15', 250.50),
    (1, '2023-02-20', 175.25),
    (2, '2023-01-10', 300.75),
    (2, '2023-03-05', 225.00)
])

# Execute a window function query to calculate cumulative spending
result = conn.execute('''
SELECT 
    customer_id, 
    order_date, 
    total_amount,
    SUM(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date) as cumulative_spend
FROM customer_orders
''').fetchall()

for row in result:
    print(row)