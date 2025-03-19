# Generated: 2025-03-19 19:41:57.795960
# Result: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table with hierarchical sales data
conn.execute('''
CREATE TABLE product_sales (
    product_id INT,
    product_name VARCHAR,
    category VARCHAR,
    sales_amount DECIMAL(10,2),
    sales_year INT
);

INSERT INTO product_sales VALUES
(1, 'Laptop', 'Electronics', 150000.50, 2022),
(2, 'Smartphone', 'Electronics', 220000.75, 2022),
(3, 'Tablet', 'Electronics', 80000.25, 2022),
(4, 'Wireless Headphones', 'Electronics', 45000.00, 2022),
(5, 'Laptop', 'Electronics', 175000.00, 2023),
(6, 'Smartphone', 'Electronics', 250000.50, 2023),
(7, 'Tablet', 'Electronics', 95000.75, 2023);
'''
)