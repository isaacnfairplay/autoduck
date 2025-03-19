# Generated: 2025-03-19 16:03:41.123453
# Result: [(2, 'Electronics', Decimal('1500.000'), 1), (4, 'Clothing', Decimal('1200.000'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate nested subquery with window function ranking
conn.execute("""
CREATE TABLE sales (
    product_id INT,
    category VARCHAR,
    sales_amount DECIMAL
);

INSERT INTO sales VALUES
    (1, 'Electronics', 1000),
    (2, 'Electronics', 1500),
    (3, 'Clothing', 800),
    (4, 'Clothing', 1200);

WITH ranked_sales AS (
    SELECT
        product_id,
        category,
        sales_amount,
        RANK() OVER (PARTITION BY category ORDER BY sales_amount DESC) as sales_rank
    FROM sales
)
SELECT * FROM ranked_sales WHERE sales_rank = 1;
""")

result = conn.fetchall()
print(result)  # Top-selling products per category