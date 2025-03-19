# Generated: 2025-03-19 12:49:25.626315
# Result: [('Electronics', 'All Regions', 9200), ('Furniture', 'All Regions', 6000), ('Total', 'All Regions', 18700), ('Electronics', 'North', 5000), ('Clothing', 'South', 3500), ('Furniture', 'West', 6000), ('Clothing', 'All Regions', 3500), ('Electronics', 'East', 4200)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE product_sales AS
SELECT * FROM (VALUES
    (1, 'Laptop', 'Electronics', 1200.50, 50),
    (2, 'Smartphone', 'Electronics', 800.25, 100),
    (3, 'Headphones', 'Electronics', 150.75, 75),
    (4, 'Desk Chair', 'Furniture', 350.00, 30),
    (5, 'Bookshelf', 'Furniture', 250.50, 20)
) AS t(product_id, product_name, category, price, stock_quantity);
''')