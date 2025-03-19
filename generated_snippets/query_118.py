# Generated: 2025-03-19 18:10:58.261415
# Result: [(2, 102, Decimal('275.25'), Decimal('275.25')), (1, 101, Decimal('150.50'), Decimal('150.50')), (3, 101, Decimal('89.99'), Decimal('240.49')), (4, 103, Decimal('450.00'), Decimal('450.00'))]
# Valid: True
import duckdb

# Connect to an in-memory database
conn = duckdb.connect(':memory:')

# Create a sample table of customer orders
conn.execute('''
    CREATE TABLE orders (
        order_id INTEGER,
        customer_id INTEGER,
        total_amount DECIMAL(10,2)
    );

    INSERT INTO orders VALUES
        (1, 101, 150.50),
        (2, 102, 275.25),
        (3, 101, 89.99),
        (4, 103, 450.00);
''')

# Use window function to calculate running total for each customer
result = conn.execute('''
    SELECT 
        order_id, 
        customer_id, 
        total_amount,
        SUM(total_amount) OVER (PARTITION BY customer_id ORDER BY order_id) as cumulative_total
    FROM orders
''').fetchall()

for row in result:
    print(row)