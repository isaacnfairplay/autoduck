# Generated: 2025-03-19 11:34:31.044038
# Result: [('Pants', Decimal('100.00'), 115.69)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create clothing products table with new entry
conn.execute('''
CREATE TABLE clothing_products (
    category VARCHAR,
    product VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO clothing_products VALUES
('Clothing', 'Shirt', 50.00),
('Clothing', 'Jeans', 75.50),
('Clothing', 'Jacket', 120.25),
('Clothing', 'Pants', 100.00);
''')

# Analyze clothing category with price comparison
result = conn.execute('''
SELECT 
    product, 
    price, 
    ROUND(price / (SELECT AVG(price) FROM clothing_products) * 100, 2) as price_percentage
FROM clothing_products
WHERE category = 'Clothing' AND product = 'Pants'
''').fetchall()

for row in result:
    print(f"{row[0]}: ${row[1]} ({row[2]}% of category avg)")