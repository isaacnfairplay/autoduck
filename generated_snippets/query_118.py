# Generated: 2025-03-19 17:49:31.610861
# Result: [('Clothing', 'Jeans', Decimal('75.50'), Decimal('120.50'), 62.66), ('Clothing', 'Shirt', Decimal('45.00'), Decimal('120.50'), 37.34), ('Electronics', 'Laptop', Decimal('1200.50'), Decimal('2000.75'), 60.0), ('Electronics', 'Smartphone', Decimal('800.25'), Decimal('2000.75'), 40.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate a table with sales data
conn.execute('''CREATE TABLE sales (
    product VARCHAR,
    category VARCHAR,
    revenue DECIMAL(10,2)
)''')

conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('Laptop', 'Electronics', 1200.50),
    ('Smartphone', 'Electronics', 800.25),
    ('Shirt', 'Clothing', 45.00),
    ('Jeans', 'Clothing', 75.50)
])

# Calculate total revenue per category using window function
result = conn.execute('''SELECT 
    category, 
    product, 
    revenue,
    SUM(revenue) OVER (PARTITION BY category) as category_total,
    ROUND(100.0 * revenue / SUM(revenue) OVER (PARTITION BY category), 2) as percentage_of_category
FROM sales
ORDER BY category, percentage_of_category DESC''').fetchall()

for row in result:
    print(row)