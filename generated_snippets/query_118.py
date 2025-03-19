# Generated: 2025-03-19 08:12:45.301366
# Result: [('Electronics', 'Laptop', Decimal('1200.00'))]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create and populate product sales table
conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
    ('Electronics', 'Laptop', 1200.00);
''')

# Query specific electronics product
result = conn.execute('''
SELECT * FROM product_sales
WHERE category = 'Electronics' AND product = 'Laptop'
''').fetchall()

for row in result:
    print(row)