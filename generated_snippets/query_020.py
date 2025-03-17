# Generated: 2025-03-16 22:12:14.101043
# Result: [('Electronics', 10, 500.0), ('Clothing', 5, 250.0), ('Home Goods', 7, 350.0)]
# Valid: True
import duckdb

# Connect to in-memory database
con = duckdb.connect(':memory:')

# Create sales table
con.execute('''
CREATE TABLE sales (
    product_id INTEGER,
    category VARCHAR,
    quantity INTEGER,
    price DECIMAL(10,2)
);
''')

# Insert sample data
con.execute('''
INSERT INTO sales VALUES
(1, 'Electronics', 10, 500.00),
(2, 'Clothing', 5, 250.00),
(3, 'Home Goods', 7, 350.00);
''')

# Perform grouped aggregation
result = con.execute('''
SELECT 
    category, 
    SUM(quantity) as total_quantity,
    AVG(price) as avg_price
FROM sales
GROUP BY category
''').fetchall()

for row in result:
    print(f'Category: {row[0]}, Total Quantity: {row[1]}, Average Price: ${row[2]:.2f}')