# Generated: 2025-03-19 17:56:29.301046
# Result: [('Tablet', 'A', 75, 1), ('Laptop', 'A', 50, 2), ('Headphones', 'B', 200, 1), ('Smartphone', 'B', 100, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate table with product inventory
conn.execute('''CREATE TABLE inventory (
    product_id INTEGER,
    product_name VARCHAR,
    quantity INTEGER,
    warehouse VARCHAR
)''')

conn.executemany('INSERT INTO inventory VALUES (?, ?, ?, ?)', [
    (1, 'Laptop', 50, 'A'),
    (2, 'Smartphone', 100, 'B'),
    (3, 'Tablet', 75, 'A'),
    (4, 'Headphones', 200, 'B')
])

# Demonstrate complex window function ranking warehouse inventory
result = conn.execute('''SELECT 
    product_name, 
    warehouse, 
    quantity,
    DENSE_RANK() OVER (PARTITION BY warehouse ORDER BY quantity DESC) as inventory_rank
FROM inventory
ORDER BY warehouse, inventory_rank''').fetchall()

for row in result:
    print(row)