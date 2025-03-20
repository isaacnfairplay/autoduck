# Generated: 2025-03-19 21:37:18.921696
# Result: [(3, 'Smartphone', 'Electronics', 100, 1), (2, 'Tablet', 'Electronics', 75, 2), (1, 'Laptop', 'Electronics', 50, 3), (4, 'Headphones', 'Accessories', 200, 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table of product inventory
conn.execute('''
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR,
    category VARCHAR,
    stock_quantity INT
)''')

# Insert sample inventory data
conn.executemany('INSERT INTO products VALUES (?, ?, ?, ?)', [
    (1, 'Laptop', 'Electronics', 50),
    (2, 'Tablet', 'Electronics', 75),
    (3, 'Smartphone', 'Electronics', 100),
    (4, 'Headphones', 'Accessories', 200)
])

# Use window functions to rank products by stock quantity within each category
result = conn.sql('''
SELECT 
    product_id,
    product_name,
    category,
    stock_quantity,
    DENSE_RANK() OVER (PARTITION BY category ORDER BY stock_quantity DESC) as stock_rank
FROM products
''').fetchall()

print(result)