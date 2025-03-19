# Generated: 2025-03-19 18:35:48.354538
# Result: [('Electronics', 3, 716.9166666666666)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products table
conn.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name VARCHAR,
        category VARCHAR,
        price DECIMAL(10,2)
    );

    INSERT INTO products VALUES
        (1, 'Laptop', 'Electronics', 1200.00),
        (2, 'Smartphone', 'Electronics', 800.50),
        (3, 'Headphones', 'Electronics', 150.25)
''');

# Demonstrate aggregate and filtering capabilities
result = conn.execute('''
    SELECT 
        category, 
        COUNT(*) as product_count,
        AVG(price) as avg_price
    FROM products
    WHERE category = 'Electronics'
    GROUP BY category
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Products: {row[1]}, Average Price: ${row[2]:.2f}")