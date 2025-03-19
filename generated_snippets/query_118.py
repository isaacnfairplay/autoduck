# Generated: 2025-03-19 08:16:10.345776
# Result: [('Electronics', 'Tablet', Decimal('500.00'))]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create product sales table with Electronics and Tablet
conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
    ('Electronics', 'Tablet', 500.00);
''')

# Query Electronics Tablet
result = conn.execute('''
SELECT * FROM product_sales
WHERE category = 'Electronics' AND product = 'Tablet'
''').fetchall()

for row in result:
    print(row)