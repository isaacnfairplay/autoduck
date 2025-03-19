# Generated: 2025-03-19 13:39:52.698668
# Result: [('Electronics', Decimal('1250.25'), Decimal('750.25')), ('Clothing', Decimal('250.50'), None), ('Home', Decimal('150.75'), None)]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create orders table with different categories
conn.execute('CREATE TABLE orders (order_id INT, category VARCHAR, amount DECIMAL(10,2))')

# Insert sample order data
conn.executemany('INSERT INTO orders VALUES (?, ?, ?)', [
    (1, 'Electronics', 500.00),
    (2, 'Clothing', 250.50),
    (3, 'Electronics', 750.25),
    (4, 'Home', 150.75)
])

# Demonstrate conditional aggregation with FILTER clause
result = conn.execute('''
    SELECT 
        category,
        SUM(amount) as total_revenue,
        SUM(amount) FILTER (WHERE amount > 500) as high_value_revenue
    FROM orders
    GROUP BY category
    ORDER BY total_revenue DESC
''').fetchall()

print(result)