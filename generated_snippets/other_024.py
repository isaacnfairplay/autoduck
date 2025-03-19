# Generated: 2025-03-19 08:42:54.323284
# Result: [('Bob', 'Chess', 1, 88, None, None), ('Bob', 'Chess', 2, 90, 88, 2), ('Alice', 'Chess', 1, 95, None, None), ('Alice', 'Chess', 2, 92, 95, -3), ('Charlie', 'Chess', 1, 85, None, None), ('Charlie', 'Chess', 2, 87, 85, 2)]
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
'''
)

# Optional: Insert sample data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', [
    (1, 'Laptop', 'Electronics', 2, 1200.50, 2401.00, '2023-06-15', 101, 'North'),
    (2, 'Tablet', 'Electronics', 1, 350.75, 350.75, '2023-06-16', 102, 'South')
])