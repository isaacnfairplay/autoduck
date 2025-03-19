# Generated: 2025-03-19 12:46:49.827611
# Result: [('Smartphone', 'Electronics', 100, 1), ('Headphones', 'Electronics', 75, 2), ('Laptop', 'Electronics', 50, 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate product inventory table
conn.execute('''
CREATE TABLE inventory (
    product_id INT,
    product_name VARCHAR,
    category VARCHAR,
    stock_quantity INT
);

INSERT INTO inventory VALUES
    (1, 'Laptop', 'Electronics', 50),
    (2, 'Smartphone', 'Electronics', 100),
    (3, 'Headphones', 'Electronics', 75),
    (4, 'Desk Chair', 'Furniture', 30);
'''
)

# Demonstrate advanced window function: dense_rank() with filtering
result = conn.execute('''
SELECT 
    product_name, 
    category, 
    stock_quantity,
    DENSE_RANK() OVER (PARTITION BY category ORDER BY stock_quantity DESC) as stock_rank
FROM inventory
WHERE stock_quantity > 40
''').fetchall()

for row in result:
    print(row)