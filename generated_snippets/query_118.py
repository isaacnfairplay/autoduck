# Generated: 2025-03-19 10:10:43.612244
# Result: [('Laptop', 'Electronics', 50, 1, 10.0), ('Smartphone', 'Electronics', 30, 2, -10.0), ('Desk Chair', 'Furniture', 25, 1, 0.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate product inventory table
conn.execute('''
    CREATE TABLE inventory (
        product_id INTEGER,
        product_name VARCHAR,
        category VARCHAR,
        stock_quantity INTEGER,
        reorder_point INTEGER
    );

    INSERT INTO inventory VALUES
        (1, 'Laptop', 'Electronics', 50, 20),
        (2, 'Smartphone', 'Electronics', 30, 15),
        (3, 'Desk Chair', 'Furniture', 25, 10);
''')

# Analyze inventory with advanced window function
result = conn.execute('''
    SELECT 
        product_name,
        category,
        stock_quantity,
        RANK() OVER (PARTITION BY category ORDER BY stock_quantity DESC) as stock_rank,
        stock_quantity - AVG(stock_quantity) OVER (PARTITION BY category) as stock_deviation
    FROM inventory
''').fetchall()

for row in result:
    print(row)