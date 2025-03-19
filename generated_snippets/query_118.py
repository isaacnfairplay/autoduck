# Generated: 2025-03-19 19:47:10.629099
# Result: [('Shirt', 75), ('Pants', 30)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with clothing category
conn.execute('''
CREATE TABLE clothing_sales (
    category VARCHAR,
    product_name VARCHAR,
    sales_quantity INT
);

INSERT INTO clothing_sales VALUES
('Clothing', 'Shirt', 50),
('Clothing', 'Pants', 30),
('Clothing', 'Shirt', 25);
'''
)

# Group and aggregate sales by clothing type
result = conn.execute('''
SELECT 
    product_name, 
    SUM(sales_quantity) as total_sales
FROM clothing_sales
WHERE category = 'Clothing'
GROUP BY product_name
''').fetchall()

print(result)