# Generated: 2025-03-19 19:10:57.305275
# Result: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate sales table
conn.sql("""
CREATE TABLE sales (
    product_id INTEGER,
    sale_date DATE,
    quantity INTEGER,
    price DECIMAL(10,2)
);

INSERT INTO sales VALUES
(1, '2023-01-15', 5, 10.50),
(1, '2023-02-20', 3, 10.50),
(2, '2023-01-22', 2, 25.00),
(2, '2023-03-10', 4, 25.00);

-- Calculate running total of sales by product using window function
SELECT 
    product_id, 
    sale_date, 
    quantity, 
    SUM(quantity * price) OVER (PARTITION BY product_id ORDER BY sale_date) AS cumulative_sales
FROM sales
ORDER BY product_id, sale_date;
""")