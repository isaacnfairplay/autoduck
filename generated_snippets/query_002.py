# Generated: 2025-03-16 22:06:32.433792
# Result: [(1, datetime.date(2023, 1, 15), 10, Decimal('50.00'), 10, 50.0), (1, datetime.date(2023, 2, 20), 15, Decimal('52.50'), 25, 51.25), (2, datetime.date(2023, 1, 10), 5, Decimal('75.00'), 5, 75.0), (2, datetime.date(2023, 3, 5), 8, Decimal('77.25'), 13, 76.125)]
# Valid: True
# Variable results: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a sample table
con.execute('''
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
    (1, 'Laptop', 999.99),
    (2, 'Smartphone', 599.50),
    (3, 'Tablet', 349.75);
''')

# Execute a simple query
results = con.execute('SELECT * FROM products WHERE price > 500').fetchall()
for row in results:
    print(row)