# Generated: 2025-03-19 08:18:48.346033
# Result: [(1, datetime.date(2023, 2, 20), Decimal('350.75'), Decimal('601.25'), 1), (2, datetime.date(2023, 3, 5), Decimal('275.00'), Decimal('450.25'), 2), (1, datetime.date(2023, 1, 15), Decimal('250.50'), Decimal('250.50'), 3), (2, datetime.date(2023, 1, 10), Decimal('175.25'), Decimal('175.25'), 4)]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create customer order table
conn.execute('''
CREATE TABLE customer_orders (
    customer_id INTEGER,
    order_date DATE,
    order_amount DECIMAL(10,2)
);

INSERT INTO customer_orders VALUES
    (1, '2023-01-15', 250.50),
    (1, '2023-02-20', 350.75),
    (2, '2023-01-10', 175.25),
    (2, '2023-03-05', 275.00);
''')

# Apply window functions for cumulative and ranked analysis
result = conn.execute('''
SELECT
    customer_id,
    order_date,
    order_amount,
    SUM(order_amount) OVER (PARTITION BY customer_id ORDER BY order_date) as cumulative_spend,
    RANK() OVER (ORDER BY order_amount DESC) as order_rank
FROM customer_orders
''').fetchall()

for row in result:
    print(row)