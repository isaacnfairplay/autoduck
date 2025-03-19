# Generated: 2025-03-19 19:13:33.581937
# Result: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate a table with product inventory
conn.sql("""
CREATE TABLE inventory (
    product_id INTEGER,
    warehouse_id INTEGER,
    stock_quantity INTEGER
);

INSERT INTO inventory VALUES
(1, 101, 500),
(1, 102, 750),
(2, 101, 250),
(2, 103, 350);

-- Calculate total stock per product using group by and sum
SELECT 
    product_id, 
    SUM(stock_quantity) AS total_stock,
    COUNT(DISTINCT warehouse_id) AS warehouse_count
FROM inventory
GROUP BY product_id
HAVING total_stock > 500;
""").show()