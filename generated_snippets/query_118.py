# Generated: 2025-03-19 11:25:02.493182
# Result: [('Laptop', 'Electronics', Decimal('1200.00'), 1), ('Smartphone', 'Electronics', Decimal('800.50'), 2), ('Headphones', 'Electronics', Decimal('150.25'), 3), ('Running Shoes', 'Sports', Decimal('120.00'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table of products
conn.execute('''
CREATE TABLE products (
    product_id INTEGER,
    name VARCHAR,
    category VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 1200.00),
(2, 'Smartphone', 'Electronics', 800.50),
(3, 'Headphones', 'Electronics', 150.25),
(4, 'Running Shoes', 'Sports', 120.00);
'''
)

# Analytical query using window functions to rank products by price within category
result = conn.execute('''
SELECT
    name,
    category,
    price,
    RANK() OVER (PARTITION BY category ORDER BY price DESC) as price_rank
FROM products
''').fetchall()

for row in result:
    print(f"{row[0]} ({row[1]}): ${row[2]} - Rank: {row[3]}")