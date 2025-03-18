# Generated: 2025-03-17 21:27:54.861476
# Result: None
# Valid: True
import duckdb

# Establish in-memory DuckDB connection
con = duckdb.connect(':memory:')

# Create sample product and sales tables
con.execute('''
    CREATE TABLE products (id INT, name VARCHAR, category VARCHAR);
    CREATE TABLE sales (product_id INT, quantity INT, price DECIMAL(10,2));

    INSERT INTO products VALUES 
        (1, 'Laptop', 'Electronics'),
        (2, 'Smartphone', 'Electronics'),
        (3, 'Headphones', 'Electronics');

    INSERT INTO sales VALUES 
        (1, 5, 1000.00),
        (2, 10, 500.00),
        (3, 15, 200.00);
''')

# Complex analytical query with window functions and joins
query = '''
    SELECT 
        p.name, 
        p.category, 
        s.quantity, 
        s.price,
        SUM(s.quantity * s.price) OVER (PARTITION BY p.category) as category_total_revenue,
        DENSE_RANK() OVER (ORDER BY s.quantity * s.price DESC) as sales_rank
    FROM products p
    JOIN sales s ON p.id = s.product_id
'''

# Execute and display results
results = con.execute(query).fetchall()
for row in results:
    print(row)