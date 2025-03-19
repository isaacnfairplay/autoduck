# Generated: 2025-03-19 08:49:45.718529
# Result: [('Laptop', 'East', 50, 1, 1), ('Desktop', 'West', 40, 2, 2), ('Phone', 'West', 75, 1, 3), ('Tablet', 'East', 30, 2, 4)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate table for multi-warehouse inventory tracking
conn.execute('CREATE TABLE warehouse_inventory (product TEXT, warehouse TEXT, quantity INT, price DECIMAL(10,2))')
conn.executemany('INSERT INTO warehouse_inventory VALUES (?, ?, ?, ?)', [
    ('Laptop', 'East', 50, 1200.50),
    ('Phone', 'West', 75, 800.25),
    ('Tablet', 'East', 30, 500.75),
    ('Desktop', 'West', 40, 1000.00)
])

# Demonstrate complex window function with multiple window specifications
result = conn.execute('''
    SELECT 
        product, 
        warehouse, 
        quantity,
        RANK() OVER (PARTITION BY warehouse ORDER BY quantity DESC) as quantity_rank,
        DENSE_RANK() OVER (ORDER BY price DESC) as price_dense_rank
    FROM warehouse_inventory
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Warehouse: {row[1]}, Quantity: {row[2]}, Quantity Rank: {row[3]}, Price Dense Rank: {row[4]}")