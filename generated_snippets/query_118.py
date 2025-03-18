# Generated: 2025-03-18 13:19:31.711856
# Result: [(3, datetime.date(2023, 3, 10), 2, 2), (1, datetime.date(2023, 1, 15), 5, 5), (1, datetime.date(2023, 2, 25), 7, 12), (2, datetime.date(2023, 2, 20), 3, 3)]
# Valid: True
import duckdb

# Connect to in-memory database
con = duckdb.connect(':memory:')

# Create sales table
con.execute('''
    CREATE TABLE sales (
        product_id INTEGER,
        sale_date DATE,
        quantity INTEGER,
        price DECIMAL(10,2)
    );
''')

# Insert sample sales data
con.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', [
    (1, '2023-01-15', 5, 50.00),
    (2, '2023-02-20', 3, 75.50),
    (1, '2023-02-25', 7, 50.00),
    (3, '2023-03-10', 2, 100.25)
])

# Analyze sales with window function
result = con.execute('''
    SELECT 
        product_id, 
        sale_date, 
        quantity, 
        SUM(quantity) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_quantity
    FROM sales
''').fetchall()

print(result)