# Generated: 2025-03-19 17:36:01.129064
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales tracking table
conn.sql("""
CREATE TABLE product_sales (
    product_id INTEGER,
    sale_date DATE,
    quantity INTEGER,
    price DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
(1, '2023-01-15', 5, 49.99),
(1, '2023-02-20', 3, 49.99),
(2, '2023-01-10', 7, 29.50);

-- Compute cumulative sales and rolling average per product
SELECT 
    product_id, 
    sale_date,
    quantity,
    SUM(quantity) OVER (PARTITION BY product_id ORDER BY sale_date) AS cumulative_sales,
    AVG(price) OVER (PARTITION BY product_id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_avg_price
FROM product_sales
""").show()
