# Generated: 2025-03-19 15:56:55.547798
# Result: []
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table of product inventory with stock levels
conn.execute('''
    CREATE TABLE inventory (
        product_id INTEGER,
        product_name VARCHAR,
        stock_level INTEGER,
        reorder_point INTEGER
    );

    INSERT INTO inventory VALUES
        (1, 'Laptop', 50, 25),
        (2, 'Smartphone', 30, 20),
        (3, 'Tablet', 15, 10)
''')

# Find products below reorder point using window ranking
result = conn.execute('''
    SELECT 
        product_name, 
        stock_level,
        reorder_point,
        RANK() OVER (ORDER BY stock_level) as stock_rank
    FROM inventory
    WHERE stock_level < reorder_point
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Stock: {row[1]}, Reorder Point: {row[2]}, Rank: {row[3]}")