# Generated: 2025-03-19 20:30:31.865559
# Result: [('Electronics', 2, 1000.625)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample table and insert data
conn.execute('''
    CREATE TABLE products (
        product_id INTEGER, 
        name VARCHAR, 
        price DECIMAL(10,2), 
        category VARCHAR
    );
''')

conn.executemany('INSERT INTO products VALUES (?, ?, ?, ?)', [
    (1, 'Laptop', 1200.50, 'Electronics'),
    (2, 'Smartphone', 800.75, 'Electronics'),
    (3, 'Headphones', 150.25, 'Accessories'),
    (4, 'Tablet', 500.00, 'Electronics')
])

# Perform a query with filtering and aggregation
result = conn.execute('''
    SELECT category, 
           COUNT(*) as product_count, 
           AVG(price) as avg_price
    FROM products
    WHERE price > 500
    GROUP BY category
''').fetchall()

print(result)