# Generated: 2025-03-19 08:54:02.275763
# Result: [('Laptop', 'Electronics', Decimal('1200.50'), 1), ('Phone', 'Electronics', Decimal('800.25'), 2), ('Tablet', 'Electronics', Decimal('500.75'), 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product table with sales tracking
conn.execute('CREATE TABLE products (id INT PRIMARY KEY, name TEXT, category TEXT, price DECIMAL(10,2), stock INT)')

# Insert sample product data
conn.executemany('INSERT INTO products VALUES (?, ?, ?, ?, ?)', [
    (1, 'Laptop', 'Electronics', 1200.50, 50),
    (2, 'Phone', 'Electronics', 800.25, 75),
    (3, 'Tablet', 'Electronics', 500.75, 30)
])

# Analyze products with window function to rank by price within category
result = conn.execute('''
    SELECT 
        name, 
        category, 
        price,
        RANK() OVER (PARTITION BY category ORDER BY price DESC) as price_rank
    FROM products
''').fetchall()

for row in result:
    print(f'Product: {row[0]}, Category: {row[1]}, Price: ${row[2]}, Price Rank: {row[3]}')