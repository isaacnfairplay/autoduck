# Generated: 2025-03-19 08:09:18.495066
# Result: [('Electronics', Decimal('24008.75'), 1000.375), ('Clothing', Decimal('3000.00'), 150.0)]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create sales dataset
conn.execute('''
CREATE TABLE sales (
    product VARCHAR,
    category VARCHAR,
    quantity INTEGER,
    price DECIMAL(10,2)
);

INSERT INTO sales VALUES
    ('Laptop', 'Electronics', 10, 1200.50),
    ('Smartphone', 'Electronics', 15, 800.25),
    ('Shoes', 'Clothing', 20, 150.00);
''')

# Analyze total sales by category
result = conn.execute('''
SELECT 
    category, 
    SUM(quantity * price) as total_revenue,
    AVG(price) as avg_price
FROM sales
GROUP BY category
''').fetchall()

for row in result:
    print(row)