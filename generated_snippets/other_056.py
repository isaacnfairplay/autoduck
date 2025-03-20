# Generated: 2025-03-19 20:35:46.795839
# Result: [(1, 'Alice', None, 0), (4, 'David', None, 0), (2, 'Bob', 1, 1), (3, 'Charlie', 1, 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table with comprehensive attributes
conn.execute('''
CREATE TABLE product_sales (
    sale_id INTEGER PRIMARY KEY,
    product_name VARCHAR,
    category VARCHAR,
    sale_date DATE,
    quantity INTEGER,
    unit_price DECIMAL(10,2),
    total_revenue DECIMAL(10,2),
    region VARCHAR
);
''')

# Insert sample sales data
conn.executemany('INSERT INTO product_sales VALUES (?, ?, ?, ?, ?, ?, ?, ?)', [
    (1, 'Laptop', 'Electronics', '2023-06-01', 2, 1200.50, 2401.00, 'North'),
    (2, 'Smartphone', 'Electronics', '2023-06-02', 3, 800.75, 2402.25, 'South'),
    (3, 'Headphones', 'Accessories', '2023-06-03', 5, 150.25, 751.25, 'East')
])