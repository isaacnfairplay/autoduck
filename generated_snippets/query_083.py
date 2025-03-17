# Generated: 2025-03-16 22:52:49.213137
# Result: [('Mid-range', 2, 799.99), ('Budget', 1, 299.99)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a table and insert data
con.execute('CREATE TABLE products (id INT, name VARCHAR, price DECIMAL(10,2))')
con.execute("INSERT INTO products VALUES (1, 'Laptop', 999.99), (2, 'Smartphone', 599.99), (3, 'Tablet', 299.99)")

# Perform a query with filtering and aggregation
result = con.execute('''
SELECT 
    CASE 
        WHEN price < 500 THEN 'Budget'
        WHEN price BETWEEN 500 AND 1000 THEN 'Mid-range'
        ELSE 'Premium'
    END as price_category,
    COUNT(*) as product_count,
    AVG(price) as average_price
FROM products
GROUP BY price_category
''').fetchall()

print(result)