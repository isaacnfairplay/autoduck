# Generated: 2025-03-19 09:25:54.984506
# Result: [(1, 'Electronics', Decimal('1200.50'), 1.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with sales data
conn.execute('''
CREATE TABLE sales (
    product_id INTEGER,
    category VARCHAR,
    sale_amount DECIMAL(10,2),
    sale_date DATE
);

INSERT INTO sales VALUES
(1, 'Electronics', 1200.50, '2023-01-15'),
(2, 'Electronics', 800.25, '2023-02-20'),
(3, 'Sports', 350.00, '2023-03-10'),
(4, 'Sports', 250.75, '2023-04-05');
''')

# Advanced filtering using window functions and subqueries
result = conn.execute('''
WITH ranked_sales AS (
    SELECT 
        product_id, 
        category, 
        sale_amount,
        PERCENT_RANK() OVER (PARTITION BY category ORDER BY sale_amount) as percentile_rank
    FROM sales
)
SELECT * FROM ranked_sales
WHERE percentile_rank > 0.5
    AND category = 'Electronics'
''').fetchall()

print(result)