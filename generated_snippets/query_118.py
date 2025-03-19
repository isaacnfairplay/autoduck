# Generated: 2025-03-19 18:46:12.980783
# Result: [('Laptop', 12, 1), ('Phone', 10, 2), ('Tablet', 3, 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table
conn.execute('CREATE TABLE sales (product VARCHAR, quantity INT, sale_date DATE)')

# Insert sample sales data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('Laptop', 5, '2023-01-15'),
    ('Phone', 10, '2023-02-20'),
    ('Tablet', 3, '2023-03-10'),
    ('Laptop', 7, '2023-04-05')
])

# Rank products by total quantity sold using DENSE_RANK()
result = conn.execute('''
    SELECT 
        product, 
        SUM(quantity) as total_quantity,
        DENSE_RANK() OVER (ORDER BY SUM(quantity) DESC) as sales_rank
    FROM sales
    GROUP BY product
''').fetchall()

print(result)