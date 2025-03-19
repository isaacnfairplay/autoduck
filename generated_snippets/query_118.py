# Generated: 2025-03-19 14:57:03.960823
# Result: [('Tablet', 30, 0.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table of product inventory
conn.execute('''CREATE TABLE inventory (
    product_id INTEGER,
    product_name VARCHAR,
    stock_quantity INTEGER,
    last_restock_date DATE
)''')

# Insert sample data
conn.execute('''INSERT INTO inventory VALUES
    (1, 'Laptop', 50, '2023-06-15'),
    (2, 'Smartphone', 75, '2023-05-20'),
    (3, 'Tablet', 30, '2023-04-10')''')

# Query to find low stock products using window function
result = conn.execute('''SELECT 
    product_name, 
    stock_quantity,
    PERCENT_RANK() OVER (ORDER BY stock_quantity) as stock_percentile
FROM inventory
WHERE stock_quantity < 50
ORDER BY stock_percentile''').fetchall()

print(result)