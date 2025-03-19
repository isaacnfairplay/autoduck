# Generated: 2025-03-19 12:26:36.573081
# Result: [('Phone', Decimal('800.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics table with task data
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

# Query products matching specific criteria
result = conn.execute('''
SELECT product, price
FROM electronics
WHERE category = 'Electronics' AND price = 800
''').fetchall()

for row in result:
    print(row)