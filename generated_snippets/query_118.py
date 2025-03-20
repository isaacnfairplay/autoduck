# Generated: 2025-03-19 20:46:51.528654
# Result: [('Electronics', 'Laptop', Decimal('1200.50')), ('Electronics', 'Smartphone', Decimal('800.75')), ('Clothing', 'Pants', Decimal('100.00')), ('Clothing', 'Shirt', Decimal('50.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table
conn.execute('CREATE TABLE product_sales (category TEXT, product TEXT, sales DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO product_sales VALUES (?, ?, ?)', [
    ('Electronics', 'Laptop', 1200.50),
    ('Electronics', 'Smartphone', 800.75),
    ('Electronics', 'Tablet', 500.25),
    ('Clothing', 'Shirt', 50.00),
    ('Clothing', 'Pants', 100.00)
])

# Use QUALIFY to get top 2 products per category by sales
result = conn.execute('''
SELECT category, product, sales
FROM (
    SELECT *,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY sales DESC) as rank
    FROM product_sales
) ranked_products
WHERE rank <= 2
''').fetchall()

print(result)