# Generated: 2025-03-19 12:28:22.092236
# Result: [('Shirt', Decimal('50.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create clothing products table
conn.execute('''
CREATE TABLE clothing (
    category VARCHAR,
    product VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO clothing VALUES
    ('Clothing', 'Shirt', 50),
    ('Clothing', 'Pants', 75),
    ('Clothing', 'Jacket', 120);
''')

# Query clothing items matching task criteria
result = conn.execute('''
SELECT product, price
FROM clothing
WHERE category = 'Clothing' AND product = 'Shirt'
''').fetchall()

for row in result:
    print(row)