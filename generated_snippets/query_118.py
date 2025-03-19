# Generated: 2025-03-19 12:25:45.563430
# Result: [('Electronics', 'Laptop', Decimal('1200.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create an electronics products table
conn.execute('''
CREATE TABLE electronics (
    category VARCHAR,
    product VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO electronics VALUES
    ('Electronics', 'Laptop', 1200.00),
    ('Electronics', 'Smartphone', 800.50),
    ('Electronics', 'Tablet', 500.25);
''')

# Find products above specific price threshold
result = conn.execute('''
SELECT category, product, price
FROM electronics
WHERE price > 1000
''').fetchall()

for row in result:
    print(row)