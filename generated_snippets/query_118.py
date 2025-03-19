# Generated: 2025-03-19 12:48:34.599423
# Result: [('Electronics', 'All Regions', 9200), ('Furniture', 'All Regions', 6000), ('Total', 'All Regions', 18700), ('Electronics', 'North', 5000), ('Clothing', 'South', 3500), ('Furniture', 'West', 6000), ('Clothing', 'All Regions', 3500), ('Electronics', 'East', 4200)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create multi-dimensional sales data
conn.execute('''
CREATE TABLE sales AS
SELECT * FROM (VALUES
    ('Electronics', 'North', 5000, '2023-Q1'),
    ('Clothing', 'South', 3500, '2023-Q1'),
    ('Electronics', 'East', 4200, '2023-Q1'),
    ('Furniture', 'West', 6000, '2023-Q1')
) AS t(category, region, revenue, quarter);
''')

# Demonstrate ROLLUP for multi-dimensional aggregation
result = conn.execute('''
SELECT 
    COALESCE(category, 'Total') as product_category,
    COALESCE(region, 'All Regions') as sales_region, 
    SUM(revenue) as total_revenue
FROM sales
GROUP BY ROLLUP(category, region)
''').fetchall()

for row in result:
    print(row)