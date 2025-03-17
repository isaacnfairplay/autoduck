# Generated: 2025-03-16 22:08:02.560731
# Result: ('Books', 1, Decimal('100.25'), 100.25)
# Valid: True
# Variable aggregate_result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a sample products table
con.execute('''
CREATE TABLE products (
    product_id INT,
    category VARCHAR,
    revenue DECIMAL(10,2)
);

INSERT INTO products VALUES
    (1, 'Electronics', 500.50),
    (2, 'Clothing', 250.75),
    (3, 'Books', 100.25);
''')

# Perform aggregate calculation on the products table
aggregate_result = con.execute('''
SELECT 
    category, 
    COUNT(*) as product_count,
    SUM(revenue) as total_revenue,
    AVG(revenue) as avg_revenue
FROM products
GROUP BY category
''').fetchall()

# Display aggregate results
for result in aggregate_result:
    print(f"Category: {result[0]}, Products: {result[1]}, Total Revenue: ${result[2]}, Avg Revenue: ${result[3]:.2f}")