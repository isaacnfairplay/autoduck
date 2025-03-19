# Generated: 2025-03-19 19:54:57.353058
# Result: [('Phone', 150, 40, 0.26666666666666666, 1), ('Laptop', 100, 25, 0.25, 2), ('Tablet', 75, 15, 0.2, 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table for tracking product inventory and sales
conn.execute('''
CREATE TABLE product_tracking (
    product_id INT,
    product_name VARCHAR,
    inventory_quantity INT,
    sales_quantity INT,
    price DECIMAL(10,2)
);

INSERT INTO product_tracking VALUES
(1, 'Laptop', 100, 25, 999.99),
(2, 'Phone', 150, 40, 599.99),
(3, 'Tablet', 75, 15, 349.99);
'''
)

# Calculate inventory turnover ratio using window functions
result = conn.execute('''
SELECT 
    product_name,
    inventory_quantity,
    sales_quantity,
    sales_quantity * 1.0 / inventory_quantity as turnover_ratio,
    RANK() OVER (ORDER BY sales_quantity * 1.0 / inventory_quantity DESC) as turnover_rank
FROM product_tracking
''').fetchall()

print(result)