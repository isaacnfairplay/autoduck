# Generated: 2025-03-18 19:40:10.413834
# Result: [('Electronics', 'Laptop', Decimal('999.99'), 799.99, 1), ('Electronics', 'Smartphone', Decimal('599.99'), 799.99, 2), ('Sports', 'Running Shoes', Decimal('129.99'), 129.99, 3)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample table of products
conn.sql("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name VARCHAR,
    category VARCHAR,
    price DECIMAL(10, 2)
);

INSERT INTO products VALUES
    (1, 'Laptop', 'Electronics', 999.99),
    (2, 'Smartphone', 'Electronics', 599.99),
    (3, 'Running Shoes', 'Sports', 129.99);
""")

# Demonstrate a complex query with window function and aggregation
result = conn.sql("""
SELECT 
    category, 
    name, 
    price,
    AVG(price) OVER (PARTITION BY category) as category_avg_price,
    RANK() OVER (ORDER BY price DESC) as price_rank
FROM products
""").fetchall()

for row in result:
    print(row)
