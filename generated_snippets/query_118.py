# Generated: 2025-03-19 11:39:53.712269
# Result: [('Clothing', 'Jeans', Decimal('75.50'), 1), ('Clothing', 'Shirt', Decimal('50.00'), 2), ('Electronics', 'Laptop', Decimal('1200.00'), 1), ('Electronics', 'Smartphone', Decimal('800.50'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and analyze product categories
conn.execute('''
CREATE TABLE product_categories (
    category VARCHAR,
    product VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO product_categories VALUES
('Electronics', 'Laptop', 1200.00),
('Electronics', 'Smartphone', 800.50),
('Clothing', 'Shirt', 50.00),
('Clothing', 'Jeans', 75.50);
''')

# Rank products by price within each category
result = conn.execute('''
SELECT
    category,
    product,
    price,
    RANK() OVER (PARTITION BY category ORDER BY price DESC) as price_rank
FROM product_categories
ORDER BY category, price_rank
''').fetchall()

for row in result:
    print(f"{row[1]} ({row[0]}): ${row[2]} - Rank: {row[3]}")