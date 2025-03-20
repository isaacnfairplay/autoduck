# Generated: 2025-03-19 20:45:07.369594
# Result: [(1, 'Laptop', Decimal('1200.50')), (2, 'Smartphone', Decimal('800.75')), (3, 'Tablet', Decimal('500.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample table
conn.execute('CREATE TABLE products (id INTEGER, name VARCHAR, price DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO products VALUES (?, ?, ?)', [
    (1, 'Laptop', 1200.50),
    (2, 'Smartphone', 800.75),
    (3, 'Tablet', 500.00)
])

# Select all rows
result = conn.execute('SELECT * FROM products').fetchall()

print(result)