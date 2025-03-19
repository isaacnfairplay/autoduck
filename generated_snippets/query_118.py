# Generated: 2025-03-19 08:37:39.881796
# Result: [('Phone', 'West', 75, 1), ('Desktop', 'West', 40, 2), ('Laptop', 'East', 50, 1), ('Tablet', 'East', 30, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate product inventory table
conn.execute('CREATE TABLE inventory (product TEXT, quantity INT, warehouse TEXT)')
conn.executemany('INSERT INTO inventory VALUES (?, ?, ?)', [
    ('Laptop', 50, 'East'), ('Phone', 75, 'West'), 
    ('Tablet', 30, 'East'), ('Desktop', 40, 'West')
])

# Use window function to rank products by quantity per warehouse
result = conn.execute('''
    SELECT 
        product, 
        warehouse, 
        quantity,
        RANK() OVER (PARTITION BY warehouse ORDER BY quantity DESC) as rank
    FROM inventory
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Warehouse: {row[1]}, Quantity: {row[2]}, Rank: {row[3]}")