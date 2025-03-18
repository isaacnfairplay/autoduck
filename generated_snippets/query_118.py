# Generated: 2025-03-17 20:07:48.516513
# Result: [(4, 'David', 'Engineering', 1, 4.0), (2, 'Bob', 'Marketing', 1, 2.0), (1, 'Alice', 'Sales', 1, 2.0), (3, 'Charlie', 'Sales', 2, 2.0)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create and populate sample table
con.execute('''
    CREATE TABLE products (
        product_id INT,
        product_name VARCHAR,
        price DECIMAL(10,2)
    );

    INSERT INTO products VALUES
        (1, 'Laptop', 1200.50),
        (2, 'Smartphone', 800.25),
        (3, 'Tablet', 500.75);
''')

# Perform complex analytical query with window functions
query = '''
    SELECT 
        product_name, 
        price,
        RANK() OVER (ORDER BY price DESC) as price_rank,
        AVG(price) OVER () as avg_product_price
    FROM products
    ORDER BY price_rank
'''

results = con.execute(query).fetchall()
for row in results:
    print(row)