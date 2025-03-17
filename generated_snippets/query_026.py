# Generated: 2025-03-16 22:17:08.161734
# Result: [('Laptop', Decimal('1200.50'), 833.8333333333334), ('Smartphone', Decimal('800.25'), 833.8333333333334), ('Tablet', Decimal('500.75'), 833.8333333333334)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a sample table
con.sql('''
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
    (1, 'Laptop', 1200.50),
    (2, 'Smartphone', 800.25),
    (3, 'Tablet', 500.75);
''')

# Execute an analytical query
result = con.sql('''
SELECT 
    name, 
    price, 
    AVG(price) OVER () AS avg_price
FROM products
''').fetchall()

for row in result:
    print(row)