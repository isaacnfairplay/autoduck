# Generated: 2025-03-19 16:29:28.810610
# Result: [(101, Decimal('75.75'), 2, 37.875)]
# Valid: True
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create a sample table of customer orders
conn.execute('''
CREATE TABLE orders (
    order_id INTEGER,
    customer_id INTEGER,
    product VARCHAR,
    order_date DATE,
    amount DECIMAL(10,2)
);

INSERT INTO orders VALUES
    (1, 101, 'Widget', '2023-01-15', 50.00),
    (2, 102, 'Gadget', '2023-02-20', 75.50),
    (3, 101, 'Sprocket', '2023-03-10', 25.75);
''')

# Demonstrate nested subquery with multiple aggregations
result = conn.execute('''
WITH customer_totals AS (
    SELECT 
        customer_id, 
        SUM(amount) as total_spend,
        COUNT(order_id) as order_count
    FROM orders
    GROUP BY customer_id
)
SELECT 
    customer_id, 
    total_spend,
    order_count,
    total_spend / order_count as avg_order_value
FROM customer_totals
WHERE total_spend > (
    SELECT AVG(total_spend) FROM customer_totals
)
''').fetchall()

for row in result:
    print(row)