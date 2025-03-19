# Generated: 2025-03-19 15:51:48.543616
# Result: [('Electronics', 2022, 50000, 50000), ('Electronics', 2023, 65000, 115000), ('Clothing', 2022, 75000, 75000), ('Clothing', 2023, 80000, 155000)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create temporary table of sales data
conn.execute('''
    CREATE TEMPORARY TABLE sales AS
    SELECT * FROM (
        VALUES
        ('Electronics', 2022, 50000),
        ('Clothing', 2022, 75000),
        ('Electronics', 2023, 65000),
        ('Clothing', 2023, 80000)
    ) AS t(category, year, revenue)
''')

# Demonstrate window function: calculate cumulative revenue per category
result = conn.execute('''
    SELECT 
        category, 
        year, 
        revenue,
        SUM(revenue) OVER (PARTITION BY category ORDER BY year) as cumulative_revenue
    FROM sales
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Year: {row[1]}, Revenue: {row[2]}, Cumulative Revenue: {row[3]}")