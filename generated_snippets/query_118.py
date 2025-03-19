# Generated: 2025-03-19 18:34:01.188795
# Result: [('Electronics', ['LAPTOP', 'TABLET', 'PHONE'], ['laptop', 'tablet', 'phone']), ('Clothing', ['SHIRT', 'PANTS', 'JACKET'], ['shirt', 'pants', 'jacket']), ('Books', ['NOVEL', 'TEXTBOOK', 'MAGAZINE'], ['novel', 'textbook', 'magazine'])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sales dataset with nested arrays
conn.sql("""
CREATE TABLE sales AS 
SELECT * FROM (
    VALUES 
    (1, 'Electronics', ['laptop', 'tablet', 'phone']),
    (2, 'Clothing', ['shirt', 'pants', 'jacket']),
    (3, 'Books', ['novel', 'textbook', 'magazine'])
) t(dept_id, department, product_array)
""")

# Demonstrate array_transform and array_filter
result = conn.sql("""
SELECT 
    department, 
    array_transform(product_array, x -> upper(x)) as capitalized_products,
    array_filter(product_array, x -> length(x) > 4) as long_products
FROM sales
""").fetchall()

for row in result:
    print(row)