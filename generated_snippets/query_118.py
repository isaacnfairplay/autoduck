# Generated: 2025-03-19 17:13:37.251038
# Result: [(2, 'Electronics', Decimal('750.00'), 1), (1, 'Electronics', Decimal('500.00'), 2), (4, 'Clothing', Decimal('200.00'), 1), (3, 'Clothing', Decimal('100.00'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create products table with sales
conn.sql("""
    CREATE TABLE products (
        product_id INTEGER,
        category VARCHAR,
        price DECIMAL(10,2)
    );

    INSERT INTO products VALUES
        (1, 'Electronics', 500.00),
        (2, 'Electronics', 750.00),
        (3, 'Clothing', 100.00),
        (4, 'Clothing', 200.00);
""")

# Rank products within category by price using DENSE_RANK()
result = conn.sql("""
    SELECT 
        product_id, 
        category, 
        price,
        DENSE_RANK() OVER (PARTITION BY category ORDER BY price DESC) as price_rank
    FROM products
""").fetchall()

for row in result:
    print(row)