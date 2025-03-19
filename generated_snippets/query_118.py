# Generated: 2025-03-19 15:34:10.118447
# Result: [('Product A', 10, '2023-01-01', 4, 10.0), ('Product A', 15, '2023-01-02', 3, 12.5), ('Product B', 20, '2023-01-03', 2, 20.0), ('Product B', 25, '2023-01-04', 1, 22.5)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Complex window function with ranking and moving aggregation
result = conn.sql("""
    WITH sales_data AS (
        SELECT 'Product A' as product, 10 as quantity, '2023-01-01' as sale_date
        UNION ALL
        SELECT 'Product A', 15, '2023-01-02'
        UNION ALL
        SELECT 'Product B', 20, '2023-01-03'
        UNION ALL
        SELECT 'Product B', 25, '2023-01-04'
    )
    SELECT 
        product, 
        quantity,
        sale_date,
        RANK() OVER (ORDER BY quantity DESC) as sales_rank,
        AVG(quantity) OVER (PARTITION BY product ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as rolling_avg
    FROM sales_data
""").fetchall()

print(result)