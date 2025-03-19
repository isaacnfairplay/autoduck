# Generated: 2025-03-19 11:15:15.233628
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    total_amount DECIMAL(10,2),
    order_date DATE
);

INSERT INTO orders VALUES
    (1, 101, 250.50, '2023-01-15'),
    (2, 102, 175.25, '2023-02-20'),
    (3, 101, 300.75, '2023-03-10');

-- Find customer spending with window functions
SELECT 
    customer_id, 
    total_amount,
    order_date,
    SUM(total_amount) OVER (PARTITION BY customer_id) as total_customer_spend,
    FIRST_VALUE(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) as first_order_date
FROM orders
''').fetchall()