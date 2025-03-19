# Generated: 2025-03-19 12:41:30.669840
# Result: [('Laptop', 'Electronics', Decimal('1200.00')), ('Smartphone', 'Electronics', Decimal('800.00')), ('Shirt', 'Clothing', Decimal('50.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales table
conn.execute('''
CREATE TABLE sales (
    product VARCHAR,
    category VARCHAR,
    amount DECIMAL(10,2)
);

INSERT INTO sales VALUES
    ('Laptop', 'Electronics', 1200.00),
    ('Smartphone', 'Electronics', 800.00),
    ('Shirt', 'Clothing', 50.00)
''')

# Fetch and print results
result = conn.execute('SELECT * FROM sales').fetchall()
for row in result:
    print(row)