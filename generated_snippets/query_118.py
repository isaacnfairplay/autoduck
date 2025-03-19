# Generated: 2025-03-19 08:07:35.033681
# Result: [(101, datetime.date(2023, 6, 15), Decimal('1200.50'), Decimal('1200.50'), 1), (102, datetime.date(2023, 6, 16), Decimal('800.25'), Decimal('800.25'), 2), (101, datetime.date(2023, 6, 17), Decimal('150.00'), Decimal('1350.50'), 3)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a table for online orders
conn.execute('''
CREATE TABLE orders (
    order_id INTEGER,
    customer_id INTEGER,
    product_name VARCHAR,
    order_date DATE,
    total_amount DECIMAL(10,2)
);

INSERT INTO orders VALUES
    (1, 101, 'Laptop', '2023-06-15', 1200.50),
    (2, 102, 'Smartphone', '2023-06-16', 800.25),
    (3, 101, 'Headphones', '2023-06-17', 150.00);
'''
)

# Perform a query with multiple window functions
result = conn.execute('''
SELECT 
    customer_id,
    order_date,
    total_amount,
    SUM(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date) as cumulative_spend,
    RANK() OVER (ORDER BY total_amount DESC) as order_rank
FROM orders
''').fetchall()

for row in result:
    print(row)