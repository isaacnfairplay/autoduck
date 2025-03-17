# Generated: 2025-03-16 22:42:55.256633
# Result: [(1, 'Laptop', Decimal('1000.50')), (3, 'Tablet', Decimal('750.75'))]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample table
conn.execute('CREATE TABLE products (id INTEGER, name VARCHAR, price DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO products VALUES (?, ?, ?)', [
    (1, 'Laptop', 1000.50),
    (2, 'Smartphone', 500.25),
    (3, 'Tablet', 750.75)
])

# Execute a query and fetch results
result = conn.execute('SELECT * FROM products WHERE price > 600').fetchall()

# Print the results
for row in result:
    print(f'Product: {row[1]}, Price: ${row[2]}')