# Generated: 2025-03-19 12:36:21.592426
# Result: [('Laptop', 'Electronics', Decimal('1200.00')), ('Chair', 'Furniture', Decimal('250.50'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE sales (
    product VARCHAR,
    category VARCHAR,
    amount DECIMAL(10,2)
);

INSERT INTO sales VALUES
    ('Laptop', 'Electronics', 1200.00),
    ('Shirt', 'Clothing', 50.00),
    ('Chair', 'Furniture', 250.50);
''')

result = conn.execute('''
SELECT product, category, amount
FROM sales
WHERE amount > 100
''').fetchall()

for row in result:
    print(row)