# Generated: 2025-03-19 15:59:27.402027
# Result: [('temperature', 98.9, 2), ('pH', 6.9, 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample table
conn.execute('''
CREATE TABLE products (
    id INTEGER,
    name VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
    (1, 'Laptop', 1200.50),
    (2, 'Smartphone', 800.25),
    (3, 'Tablet', 500.75)
''')

# Create a relation and print results
rel = conn.sql('SELECT name, price FROM products WHERE price > 1000')
print(rel.execute().fetchall())