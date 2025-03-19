# Generated: 2025-03-19 09:23:50.836516
# Result: [(102, datetime.date(2023, 1, 10), Decimal('350.25'), 1), (102, datetime.date(2023, 3, 5), Decimal('175.00'), 2), (101, datetime.date(2023, 1, 15), Decimal('250.50'), 1), (101, datetime.date(2023, 2, 20), Decimal('125.75'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('''
    CREATE TABLE orders (
        order_id INTEGER,
        customer_id INTEGER,
        total_amount DECIMAL(10,2),
        order_date DATE
    );

    INSERT INTO orders VALUES
    (1, 101, 250.50, '2023-01-15'),
    (2, 101, 125.75, '2023-02-20'),
    (3, 102, 350.25, '2023-01-10'),
    (4, 102, 175.00, '2023-03-05');
''')

result = conn.execute('''
    SELECT 
        customer_id, 
        order_date, 
        total_amount,
        DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY total_amount DESC) as order_rank
    FROM orders
''').fetchall()

print(result)