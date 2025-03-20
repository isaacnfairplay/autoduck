# Generated: 2025-03-19 20:00:09.884705
# Result: [('Electronics', 'Laptop', Decimal('1200.50'), 1), ('Electronics', 'Phone', Decimal('800.25'), 2), ('Electronics', 'Tablet', Decimal('500.00'), 3), ('Clothing', 'Pants', Decimal('120.50'), 1), ('Clothing', 'Shirt', Decimal('75.00'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales data with rankings
conn.execute('CREATE TABLE product_sales (category TEXT, product TEXT, sales DECIMAL(10,2))')
conn.executemany('INSERT INTO product_sales VALUES (?, ?, ?)', [
    ['Electronics', 'Laptop', 1200.50],
    ['Electronics', 'Phone', 800.25],
    ['Electronics', 'Tablet', 500.00],
    ['Clothing', 'Shirt', 75.00],
    ['Clothing', 'Pants', 120.50]
])

# Rank products within category by sales
result = conn.execute('''SELECT 
    category, 
    product, 
    sales, 
    RANK() OVER (PARTITION BY category ORDER BY sales DESC) as sales_rank
FROM product_sales
''').fetchall()

for row in result:
    print(row)