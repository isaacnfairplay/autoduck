# Generated: 2025-03-19 11:35:24.758683
# Result: [('Clothing', 'Jeans', Decimal('75.50'), 60.16), ('Clothing', 'Shirt', Decimal('50.00'), 39.84), ('Electronics', 'Laptop', Decimal('1500.00'), 63.82), ('Electronics', 'Smartphone', Decimal('850.50'), 36.18)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create temporary product sales table
conn.execute('''
CREATE TABLE product_sales AS
SELECT 'Electronics' as category, 'Laptop' as product, 1500.00 as amount
UNION ALL
SELECT 'Electronics', 'Smartphone', 850.50
UNION ALL
SELECT 'Clothing', 'Jeans', 75.50
UNION ALL
SELECT 'Clothing', 'Shirt', 50.00
''')

# Analyze product sales with total and percentage
result = conn.execute('''
SELECT
    category,
    product,
    amount,
    ROUND(amount / SUM(amount) OVER (PARTITION BY category) * 100, 2) as category_percentage
FROM product_sales
ORDER BY category, amount DESC
''').fetchall()

for row in result:
    print(f"{row[1]} ({row[0]}): ${row[2]} ({row[3]}% of category sales)")