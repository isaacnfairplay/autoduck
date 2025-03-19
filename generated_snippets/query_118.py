# Generated: 2025-03-19 11:53:05.752885
# Result: [(1, 'Electronics', Decimal('1500.50'), Decimal('1500.50')), (3, 'Electronics', Decimal('2200.75'), Decimal('3701.25')), (4, 'Books', Decimal('350.00'), Decimal('350.00')), (2, 'Clothing', Decimal('850.25'), Decimal('850.25'))]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create table with product sales data
conn.execute('CREATE TABLE product_sales (product_id INT, category TEXT, sales DECIMAL(10,2))')
conn.executemany('INSERT INTO product_sales VALUES (?, ?, ?)', [
    (1, 'Electronics', 1500.50),
    (2, 'Clothing', 850.25),
    (3, 'Electronics', 2200.75),
    (4, 'Books', 350.00)
])

# Use window function to calculate category-wise running total
result = conn.execute('''
    SELECT 
        product_id, 
        category, 
        sales, 
        SUM(sales) OVER (PARTITION BY category ORDER BY sales) as running_category_total
    FROM product_sales
''').fetchall()

print(result)