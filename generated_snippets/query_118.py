# Generated: 2025-03-19 12:31:02.827136
# Result: []
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table for tracking product inventory
conn.execute('''
CREATE TABLE inventory (
    product_id INT,
    product_name VARCHAR,
    quantity INT,
    reorder_level INT
);

INSERT INTO inventory VALUES
    (1, 'Laptop', 50, 20),
    (2, 'Monitor', 75, 30),
    (3, 'Keyboard', 100, 25);
''')

# Find products below reorder threshold
result = conn.execute('''
SELECT product_name, quantity, reorder_level
FROM inventory
WHERE quantity < reorder_level
''').fetchall()

for row in result:
    print(row)