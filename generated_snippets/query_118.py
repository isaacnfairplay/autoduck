# Generated: 2025-03-19 09:22:52.421880
# Result: [('Laptop', 'Electronics', Decimal('1200.50'), 1), ('Smartphone', 'Electronics', Decimal('800.25'), 2), ('Headphones', 'Electronics', Decimal('150.75'), 3), ('Running Shoes', 'Sports', Decimal('120.00'), 1)]
# Valid: True
import duckdb

# Create an in-memory database and table with product sales
conn = duckdb.connect(':memory:')
conn.execute('''
    CREATE TABLE product_sales (
        product_id INTEGER,
        product_name VARCHAR,
        category VARCHAR,
        sale_amount DECIMAL(10,2)
    );

    INSERT INTO product_sales VALUES
    (1, 'Laptop', 'Electronics', 1200.50),
    (2, 'Smartphone', 'Electronics', 800.25),
    (3, 'Headphones', 'Electronics', 150.75),
    (4, 'Running Shoes', 'Sports', 120.00);
''')

# Demonstrate window function: ranking sales within categories
result = conn.execute('''
    SELECT 
        product_name, 
        category, 
        sale_amount,
        RANK() OVER (PARTITION BY category ORDER BY sale_amount DESC) as sales_rank
    FROM product_sales
''').fetchall()

print(result)