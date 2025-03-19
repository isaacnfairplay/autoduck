# Generated: 2025-03-19 19:54:05.092134
# Result: [('Electronics', 'Phone', Decimal('1500.00'), 1), ('Electronics', 'Laptop', Decimal('1200.00'), 2), ('Clothing', 'Pants', Decimal('950.00'), 1), ('Clothing', 'Shirt', Decimal('800.00'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE sales (
    category VARCHAR,
    product VARCHAR,
    amount DECIMAL(10,2)
);

INSERT INTO sales VALUES
('Electronics', 'Laptop', 1200),
('Electronics', 'Phone', 1500),
('Electronics', 'Tablet', 900),
('Clothing', 'Shirt', 800),
('Clothing', 'Pants', 950);
''')

result = conn.execute('''
SELECT category, product, amount,
       ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC) as rank
FROM sales
QUALIFY rank <= 2
''').fetchall()

print(result)