# Generated: 2025-03-19 20:47:42.643315
# Result: [('Electronics', Decimal('2001.25')), ('Clothing', Decimal('200.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a products table with sales data
conn.execute('CREATE TABLE products (category TEXT, product TEXT, sales DECIMAL(10,2))')

# Insert sample electronics and clothing sales data
conn.executemany('INSERT INTO products VALUES (?, ?, ?)', [
    ('Electronics', 'Laptop', 1200.50),
    ('Electronics', 'Smartphone', 800.75),
    ('Clothing', 'Shirt', 50.00),
    ('Clothing', 'Jacket', 150.25)
])

# Calculate total sales per category using GROUP BY
result = conn.execute('SELECT category, SUM(sales) as total_category_sales FROM products GROUP BY category').fetchall()

print(result)