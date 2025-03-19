# Generated: 2025-03-19 09:32:09.792515
# Result: [(1, 'Laptop', 'Electronics', 'Computers', 1), (2, 'Smartphone', 'Electronics', 'Mobile', 1), (3, 'Tablet', 'Electronics', 'Computers', 1), (4, 'Running Shoes', 'Sportswear', 'Footwear', 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample products table with hierarchical categories
conn.sql("""
CREATE TABLE products (
    product_id INTEGER,
    name VARCHAR,
    category VARCHAR,
    subcategory VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
    (1, 'Laptop', 'Electronics', 'Computers', 1200.00),
    (2, 'Smartphone', 'Electronics', 'Mobile', 800.00),
    (3, 'Tablet', 'Electronics', 'Computers', 500.00),
    (4, 'Running Shoes', 'Sportswear', 'Footwear', 150.00)
""")

# Use recursive CTE to generate product hierarchies
result = conn.sql("""
WITH RECURSIVE product_hierarchy AS (
    SELECT product_id, name, category, subcategory, 1 as depth
    FROM products
    
    UNION ALL
    
    SELECT p.product_id, p.name, p.category, p.subcategory, ph.depth + 1
    FROM products p, product_hierarchy ph
    WHERE p.category = ph.subcategory
)
SELECT * FROM product_hierarchy
""").fetchall()

print(result)