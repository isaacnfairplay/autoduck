# Generated: 2025-03-19 11:33:39.876590
# Result: [('Jacket', Decimal('120.25'), 146.8), ('Jeans', Decimal('75.50'), 92.17), ('Shirt', Decimal('50.00'), 61.04)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create clothing products table
conn.execute('''
CREATE TABLE clothing_products (
    category VARCHAR,
    product VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO clothing_products VALUES
('Clothing', 'Shirt', 50.00),
('Clothing', 'Jeans', 75.50),
('Clothing', 'Jacket', 120.25);
''');

# Analyze clothing category with price comparison
result = conn.execute('''
SELECT 
    product, 
    price, 
    ROUND(price / (SELECT AVG(price) FROM clothing_products) * 100, 2) as price_percentage
FROM clothing_products
WHERE category = 'Clothing'
ORDER BY price DESC
''').fetchall()

for row in result:
    print(f"{row[0]}: ${row[1]} ({row[2]}% of category avg)")