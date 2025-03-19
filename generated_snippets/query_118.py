# Generated: 2025-03-19 16:46:11.206913
# Result: [(1, datetime.date(2023, 1, 15), 5, 5, 10.5), (1, datetime.date(2023, 3, 10), 7, 12, 10.5), (2, datetime.date(2023, 2, 20), 3, 3, 25.75)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample sales table
conn.execute('''
    CREATE TABLE sales (
        product_id INT,
        sale_date DATE,
        quantity INT,
        price DECIMAL(10,2)
    );
''')

# Insert sample data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', [
    (1, '2023-01-15', 5, 10.50),
    (2, '2023-02-20', 3, 25.75),
    (1, '2023-03-10', 7, 10.50)
])

# Perform a window function analysis
result = conn.execute('''
    SELECT 
        product_id, 
        sale_date, 
        quantity,
        SUM(quantity) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_quantity,
        AVG(price) OVER (PARTITION BY product_id) as avg_product_price
    FROM sales
''').fetchall()

print(result)