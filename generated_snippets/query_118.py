# Generated: 2025-03-19 15:07:24.350631
# Result: [(2, datetime.date(2023, 1, 10), Decimal('250.25'), Decimal('250.25'), 1), (2, datetime.date(2023, 3, 5), Decimal('350.75'), Decimal('601.00'), 2), (1, datetime.date(2023, 1, 15), Decimal('500.00'), Decimal('500.00'), 3), (1, datetime.date(2023, 2, 20), Decimal('750.50'), Decimal('1250.50'), 4)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample order data
conn.execute('CREATE TABLE orders (customer_id INT, order_date DATE, order_total DECIMAL(10,2))')
conn.executemany('INSERT INTO orders VALUES (?, ?, ?)', [
    (1, '2023-01-15', 500.00),
    (1, '2023-02-20', 750.50),
    (2, '2023-01-10', 250.25),
    (2, '2023-03-05', 350.75)
])

# Custom window function to calculate customer's cumulative spending and spending percentile
result = conn.execute('''
    SELECT 
        customer_id, 
        order_date, 
        order_total,
        SUM(order_total) OVER (PARTITION BY customer_id ORDER BY order_date) as cumulative_spending,
        NTILE(4) OVER (ORDER BY order_total) as spending_quartile
    FROM orders
''').fetchall()

for row in result:
    print(f'Customer: {row[0]}, Date: {row[1]}, Total: ${row[2]}, Cumulative: ${row[3]}, Quartile: {row[4]}')