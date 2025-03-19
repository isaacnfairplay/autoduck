# Generated: 2025-03-19 09:18:34.773676
# Result: [('Electronics', 'Laptop', Decimal('1200.50'), 1200.5), ('Electronics', 'Phone', Decimal('800.25'), 800.25), ('Electronics', 'Tablet', Decimal('600.00'), 600.0), ('Clothing', 'Shirt', Decimal('50.75'), 50.75)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with dimensional data
conn.execute('CREATE TABLE sales (product TEXT, category TEXT, amount DECIMAL(10,2), sale_date DATE)')

# Insert sample sales data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', [
    ('Laptop', 'Electronics', 1200.50, '2023-07-15'),
    ('Phone', 'Electronics', 800.25, '2023-07-16'),
    ('Tablet', 'Electronics', 600.00, '2023-07-17'),
    ('Shirt', 'Clothing', 50.75, '2023-07-18')
])

# Perform multi-dimensional sales analysis
result = conn.execute('''
SELECT
    category,
    product,
    SUM(amount) as total_sales,
    AVG(amount) as average_sale
FROM sales
GROUP BY category, product
ORDER BY total_sales DESC
''').fetchall()

for row in result:
    print(f'Category: {row[0]}, Product: {row[1]}, Total Sales: ${row[2]}, Avg Sale: ${row[3]:.2f}')