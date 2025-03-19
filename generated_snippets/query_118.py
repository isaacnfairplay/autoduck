# Generated: 2025-03-19 11:52:13.714702
# Result: [(2, 102, Decimal('275.75'), 1), (1, 101, Decimal('150.50'), 1), (3, 101, Decimal('89.99'), 2)]
# Valid: True
import duckdb

# Create an in-memory database and sample data
conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE orders (order_id INT, customer_id INT, total_amount DECIMAL(10,2))')
conn.executemany('INSERT INTO orders VALUES (?, ?, ?)', [(1, 101, 150.50), (2, 102, 275.75), (3, 101, 89.99)])

# Demonstrate window function to rank orders per customer
result = conn.execute('''
    SELECT 
        order_id, 
        customer_id, 
        total_amount,
        RANK() OVER (PARTITION BY customer_id ORDER BY total_amount DESC) as order_rank
    FROM orders
''').fetchall()

print(result)