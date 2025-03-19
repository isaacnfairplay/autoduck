# Generated: 2025-03-19 13:36:29.370918
# Result: [('Laptop', Decimal('49999.50'), 999.99), ('Phone', Decimal('49950.00'), 499.5), ('Tablet', Decimal('22481.25'), 299.75)]
# Valid: True
import duckdb

# Create in-memory database and table
conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE sales (product VARCHAR, quantity INT, price DECIMAL(10,2))')

# Insert sample sales data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('Laptop', 50, 999.99),
    ('Phone', 100, 499.50),
    ('Tablet', 75, 299.75)
])

# Calculate total revenue per product using SQL aggregation
result = conn.execute('''
    SELECT 
        product, 
        SUM(quantity * price) as total_revenue,
        AVG(price) as avg_price
    FROM sales
    GROUP BY product
    ORDER BY total_revenue DESC
''').fetchall()

print(result)