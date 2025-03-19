# Generated: 2025-03-19 11:32:48.835140
# Result: [('Laptop', Decimal('1200.50'), 366.75), ('Phone', Decimal('800.00'), -33.75), ('Tablet', Decimal('500.75'), -333.0)]
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
('Electronics', 'Phone', 800.00),
('Electronics', 'Laptop', 1200.50),
('Electronics', 'Tablet', 500.75);
''')

# Analyze products in Electronics category
result = conn.execute('''
SELECT 
    product, 
    price, 
    price - AVG(price) OVER () as price_diff
FROM electronics
WHERE category = 'Electronics'
ORDER BY price_diff DESC
''').fetchall()

for row in result:
    print(f"{row[0]}: ${row[1]} (Difference from Avg: ${row[2]:.2f})")