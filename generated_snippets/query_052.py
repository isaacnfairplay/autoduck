# Generated: 2025-03-16 22:44:03.285173
# Result: [(1, 18, 25.5, 2), (2, 5, 30.75, 1)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample sales table
conn.execute('''CREATE TABLE sales (product_id INTEGER, sale_date DATE, quantity INTEGER, price DECIMAL(10,2))''')

# Insert sample data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', [
    (1, '2023-01-15', 10, 25.50),
    (2, '2023-02-20', 5, 30.75),
    (1, '2023-03-10', 8, 25.50)
])

# Perform aggregation query
result = conn.execute('''
SELECT 
    product_id, 
    SUM(quantity) as total_quantity,
    AVG(price) as avg_price,
    COUNT(*) as sales_count
FROM sales
GROUP BY product_id
''').fetchall()

for row in result:
    print(f'Product {row[0]}: Total Quantity={row[1]}, Avg Price=${row[2]:.2f}, Sales Count={row[3]}')