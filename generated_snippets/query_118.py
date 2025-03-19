# Generated: 2025-03-19 11:31:57.243137
# Result: [('Electronics', 'Laptop', Decimal('1200.00'), 143.93), ('Electronics', 'Smartphone', Decimal('800.50'), 96.01), ('Electronics', 'Tablet', Decimal('500.75'), 60.06)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics products table
conn.execute('''
CREATE TABLE electronics_products (
    category VARCHAR,
    product VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO electronics_products VALUES
('Electronics', 'Laptop', 1200.00),
('Electronics', 'Smartphone', 800.50),
('Electronics', 'Tablet', 500.75);
''')

# Query to filter and analyze Electronics category
result = conn.execute('''
SELECT 
    category, 
    product, 
    price,
    ROUND(price / (SELECT AVG(price) FROM electronics_products) * 100, 2) as price_percentage
FROM electronics_products
ORDER BY price DESC
''').fetchall()

for row in result:
    print(f"{row[1]} ({row[0]}): ${row[2]} ({row[3]}% of avg price)")