# Generated: 2025-03-19 16:15:31.661025
# Result: [(1, Decimal('100.50'), datetime.date(2023, 1, 15), Decimal('100.50')), (1, Decimal('250.75'), datetime.date(2023, 2, 20), Decimal('351.25')), (2, Decimal('75.25'), datetime.date(2023, 3, 10), Decimal('75.25')), (2, Decimal('125.00'), datetime.date(2023, 4, 5), Decimal('200.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create temporary table for customer orders
conn.execute('''
    CREATE TABLE orders (
        customer_id INT,
        order_total DECIMAL(10,2),
        order_date DATE
    );

    INSERT INTO orders VALUES
        (1, 100.50, '2023-01-15'),
        (1, 250.75, '2023-02-20'),
        (2, 75.25, '2023-03-10'),
        (2, 125.00, '2023-04-05');
''')

# Use window function to calculate running total per customer
result = conn.execute('''
    SELECT 
        customer_id, 
        order_total, 
        order_date,
        SUM(order_total) OVER (PARTITION BY customer_id ORDER BY order_date) as running_total
    FROM orders
''').fetchall()

for row in result:
    print(f"Customer {row[0]}: Order ${row[1]} on {row[2]}, Running Total: ${row[3]})")