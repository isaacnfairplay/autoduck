# Generated: 2025-03-16 22:41:40.507675
# Result: [(1, 2, 18, 25.5, Decimal('25.50')), (2, 1, 5, 30.75, Decimal('30.75'))]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample sales table
conn.execute('''
CREATE TABLE sales (
    product_id INTEGER,
    sale_date DATE,
    quantity INTEGER,
    price DECIMAL(10,2)
)''')

# Insert sample data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', [
    (1, '2023-01-15', 10, 25.50),
    (2, '2023-02-20', 5, 30.75),
    (1, '2023-03-10', 8, 25.50)
])

# Perform complex aggregation with multiple metrics
result = conn.execute('''
SELECT 
    product_id, 
    COUNT(*) as total_sales,
    SUM(quantity) as total_quantity,
    AVG(price) as avg_price,
    MAX(price) as max_price
FROM sales
GROUP BY product_id
''').fetchall()

for row in result:
    print(f'Product {row[0]}: Sales={row[1]}, Quantity={row[2]}, Avg Price=${row[3]:.2f}, Max Price=${row[4]:.2f}')