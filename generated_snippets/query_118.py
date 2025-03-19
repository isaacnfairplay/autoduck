# Generated: 2025-03-19 18:30:34.465250
# Result: ('Clothing', Decimal('7500.000'), 3750.0)
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate multi-level nested aggregation
conn.execute('''CREATE TABLE product_sales (
    category TEXT,
    subcategory TEXT,
    sales DECIMAL
);

INSERT INTO product_sales VALUES
    ('Electronics', 'Laptops', 5000),
    ('Electronics', 'Smartphones', 7500),
    ('Clothing', 'Mens', 3000),
    ('Clothing', 'Womens', 4500);
''')

query = '''
SELECT 
    category, 
    SUM(sales) as total_category_sales,
    AVG(sales) as avg_subcategory_sales
FROM product_sales
GROUP BY category
ORDER BY total_category_sales DESC;
'''

results = conn.execute(query).fetchall()
for result in results:
    print(f'Category: {result[0]}, Total Sales: {result[1]}, Avg Subcategory Sales: {result[2]}')