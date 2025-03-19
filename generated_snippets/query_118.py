# Generated: 2025-03-19 08:56:39.220310
# Result: [('Electronics', Decimal('2751.75'), 775.625, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with comprehensive columns
conn.execute('''
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    product_name VARCHAR,
    category VARCHAR,
    quantity INTEGER,
    unit_price DECIMAL(10,2),
    total_price DECIMAL(10,2),
    sale_date DATE,
    customer_id INTEGER,
    region VARCHAR
);
''')

# Insert sample sales data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', [
    (1, 'Laptop', 'Electronics', 2, 1200.50, 2401.00, '2023-06-15', 101, 'North'),
    (2, 'Tablet', 'Electronics', 1, 350.75, 350.75, '2023-06-16', 102, 'South')
])

# Query to demonstrate flexible table exploration
result = conn.execute('''
SELECT 
    category, 
    SUM(total_price) as total_revenue, 
    AVG(unit_price) as avg_unit_price,
    COUNT(*) as num_sales
FROM sales
GROUP BY category
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Total Revenue: ${row[1]:.2f}, Avg Unit Price: ${row[2]:.2f}, Sales Count: {row[3]}")