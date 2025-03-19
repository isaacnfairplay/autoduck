# Generated: 2025-03-19 08:26:10.384594
# Result: [('Laptop', 'Electronics', 10, Decimal('1200.50')), ('Smartphone', 'Electronics', 15, Decimal('800.25')), ('Shoes', 'Clothing', 20, Decimal('150.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE sales (
    product VARCHAR,
    category VARCHAR,
    quantity INTEGER,
    price DECIMAL(10,2)
);

INSERT INTO sales VALUES
    ('Laptop', 'Electronics', 10, 1200.50),
    ('Smartphone', 'Electronics', 15, 800.25),
    ('Shoes', 'Clothing', 20, 150.00);
''')

result = conn.execute('SELECT * FROM sales').fetchall()
for row in result:
    print(row)