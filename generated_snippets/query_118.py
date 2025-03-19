# Generated: 2025-03-19 12:27:28.363787
# Result: [('Phone', Decimal('800.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics table
conn.execute('''
CREATE TABLE electronics (
    category VARCHAR,
    product VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO electronics VALUES
    ('Electronics', 'Phone', 800),
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Tablet', 500);
''')

# Filter products matching price criteria
result = conn.execute('''
SELECT product, price
FROM electronics
WHERE category = 'Electronics' AND price = 800
''').fetchall()

for row in result:
    print(row)