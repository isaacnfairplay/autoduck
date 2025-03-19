# Generated: 2025-03-19 12:47:41.571242
# Result: [('Smartphone', 'Electronics', 100, 1), ('Headphones', 'Electronics', 75, 2), ('Laptop', 'Electronics', 50, 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales data with multiple attributes
conn.execute('''
CREATE TABLE regional_sales AS
SELECT * FROM (VALUES
    (1, 'North', 'Electronics', 5000, '2023-Q1'),
    (2, 'South', 'Clothing', 3500, '2023-Q1'),
    (3, 'East', 'Electronics', 4200, '2023-Q1'),
    (4, 'West', 'Furniture', 6000, '2023-Q1'),
    (5, 'North', 'Clothing', 2800, '2023-Q1')
) AS t(sale_id, region, category, revenue, quarter);
''')