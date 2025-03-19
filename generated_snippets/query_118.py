# Generated: 2025-03-19 19:48:03.764448
# Result: [('Pants', 'South', 70), ('Shirt', 'North', 50), ('Pants', 'North', 30), ('Shirt', 'South', 25)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create clothing sales table with complex data
conn.execute('''
CREATE TABLE clothing_sales (
    category VARCHAR,
    product_name VARCHAR,
    sales_quantity INT,
    sales_region VARCHAR
);

INSERT INTO clothing_sales VALUES
('Clothing', 'Shirt', 50, 'North'),
('Clothing', 'Pants', 30, 'North'),
('Clothing', 'Shirt', 25, 'South'),
('Clothing', 'Pants', 70, 'South');
''')

# Compute total sales quantity by clothing type and region
result = conn.execute('''
SELECT 
    product_name, 
    sales_region,
    SUM(sales_quantity) as total_sales
FROM clothing_sales
WHERE category = 'Clothing'
GROUP BY product_name, sales_region
ORDER BY total_sales DESC
''').fetchall()

print(result)