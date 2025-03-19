# Generated: 2025-03-19 12:37:13.271081
# Result: [('Laptop', 'Electronics', Decimal('1200.00'), 1), ('Chair', 'Furniture', Decimal('250.50'), 2), ('Shirt', 'Clothing', Decimal('50.00'), 3)]
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
SELECT 
    product, 
    category, 
    amount,
    RANK() OVER (ORDER BY amount DESC) as overall_rank
FROM sales
''').fetchall()

for row in result:
    print(row)