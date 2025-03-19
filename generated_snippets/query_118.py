# Generated: 2025-03-19 10:46:45.619974
# Result: []
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table for tracking product inventory
conn.execute('''
CREATE TABLE inventory (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    quantity INTEGER,
    reorder_level INTEGER
);
''')

# Insert sample inventory data
conn.executemany('INSERT INTO inventory VALUES (?, ?, ?, ?)', [
    (1, 'Laptop', 50, 20),
    (2, 'Phone', 75, 30),
    (3, 'Tablet', 40, 15)
])

# Find products below reorder level
result = conn.execute('''
SELECT product_name, quantity, reorder_level
FROM inventory
WHERE quantity < reorder_level
''').fetchall()

for row in result:
    print(f'{row[0]} needs restocking: {row[1]} units (Reorder level: {row[2]})')