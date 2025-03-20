# Generated: 2025-03-19 20:32:17.350348
# Result: [(102, datetime.date(2023, 5, 16), 'Smartphone', Decimal('800.50'), Decimal('800.50')), (101, datetime.date(2023, 5, 15), 'Laptop', Decimal('2400.99'), Decimal('2400.99')), (101, datetime.date(2023, 5, 17), 'Headphones', Decimal('450.75'), Decimal('2851.74'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table for order tracking
conn.execute('''
CREATE TABLE orders (
    order_id INTEGER,
    customer_id INTEGER,
    product_name VARCHAR,
    order_date DATE,
    quantity INTEGER,
    total_price DECIMAL(10,2)
);
''')

# Insert sample order data
conn.executemany('INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?)', [
    (1, 101, 'Laptop', '2023-05-15', 2, 2400.99),
    (2, 102, 'Smartphone', '2023-05-16', 1, 800.50),
    (3, 101, 'Headphones', '2023-05-17', 3, 450.75)
])

# Perform complex analytics query with window functions
result = conn.execute('''
SELECT 
    customer_id,
    order_date,
    product_name,
    total_price,
    SUM(total_price) OVER (PARTITION BY customer_id ORDER BY order_date) as cumulative_spend
FROM orders
''').fetchall()

print(result)