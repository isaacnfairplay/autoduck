# Generated: 2025-03-16 22:49:04.140812
# Result: [('Electronics', 2, 900.0), ('Furniture', 1, 250.0)]
# Valid: True
import duckdb

# Create an in-memory DuckDB connection
conn = duckdb.connect(':memory:')

# Create a table and insert sample data
conn.execute('''
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR,
    category VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
    (1, 'Laptop', 'Electronics', 1000.00),
    (2, 'Smartphone', 'Electronics', 800.00),
    (3, 'Desk', 'Furniture', 250.00);
''')

# Perform a query with aggregation and filtering
result = conn.execute('''
SELECT 
    category, 
    COUNT(*) as product_count, 
    AVG(price) as avg_price
FROM products
GROUP BY category
HAVING COUNT(*) > 0
''').fetchall()

print(result)