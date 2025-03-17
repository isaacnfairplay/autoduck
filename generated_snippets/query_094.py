# Generated: 2025-03-16 23:55:23.397326
# Result: [(1, 'Alice', 30), (3, 'Charlie', 35)]
# Valid: True
# Variable filtered_results: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a sample table
con.execute('''
    CREATE TABLE products (
        id INT,
        name VARCHAR,
        price DECIMAL(10,2)
    );
    INSERT INTO products VALUES
        (1, 'Laptop', 1000.00),
        (2, 'Phone', 500.00),
        (3, 'Tablet', 300.00);
''')

# Filtering method demonstrating advanced query capabilities
filtered_results = con.execute('''
    SELECT * FROM products
    WHERE price > 400
    ORDER BY price DESC
''').fetchall()

for product in filtered_results:
    print(f'Product: {product[1]}, Price: ${product[2]}')