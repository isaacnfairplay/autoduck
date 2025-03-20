# Generated: 2025-03-19 21:39:59.377303
# Result: [('Clothing', '2023-Q1', 2300, 2300, 1), ('Clothing', '2023-Q2', 2100, 4400, 2), ('Electronics', '2023-Q2', 1800, 3300, 3), ('Electronics', '2023-Q1', 1500, 1500, 4)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data with different product categories
conn.execute("""CREATE TABLE sales AS
    SELECT 'Electronics' as category, 1500 as revenue, '2023-Q1' as quarter
    UNION ALL
    SELECT 'Clothing', 2300, '2023-Q1'
    UNION ALL
    SELECT 'Electronics', 1800, '2023-Q2'
    UNION ALL
    SELECT 'Clothing', 2100, '2023-Q2'""")

# Analyze sales using window functions and aggregations
result = conn.execute("""SELECT 
    category, 
    quarter, 
    revenue,
    SUM(revenue) OVER (PARTITION BY category ORDER BY quarter) as cumulative_revenue,
    RANK() OVER (ORDER BY revenue DESC) as revenue_rank
FROM sales""").fetchall()

for row in result:
    print(row)