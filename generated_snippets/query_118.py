# Generated: 2025-03-18 14:49:50.863134
# Result: [('Electronics', datetime.date(2023, 1, 15), Decimal('2500.00'), Decimal('2500.00'), 1), ('Electronics', datetime.date(2023, 2, 20), Decimal('1500.50'), Decimal('4000.50'), 2), ('Electronics', datetime.date(2023, 3, 10), Decimal('1000.25'), Decimal('5000.75'), 3)]
# Valid: True
import duckdb

# Connect to in-memory database
con = duckdb.connect(':memory:')

# Create sales and product tables
con.execute('CREATE TABLE products (id INTEGER PRIMARY KEY, name VARCHAR, category VARCHAR)')
con.execute('CREATE TABLE sales (product_id INTEGER, sale_date DATE, quantity INTEGER, total_price DECIMAL(10,2))')

# Insert sample data
con.executemany('INSERT INTO products VALUES (?, ?, ?)', [
    (1, 'Laptop', 'Electronics'),
    (2, 'Smartphone', 'Electronics'),
    (3, 'Desk Chair', 'Furniture')
])

con.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', [
    (1, '2023-01-15', 5, 2500.00),
    (2, '2023-02-20', 3, 1500.50),
    (1, '2023-03-10', 2, 1000.25)
])

# Complex query with join, window function, and aggregation
result = con.execute('''
    SELECT 
        p.category, 
        sale_date, 
        total_price,
        SUM(total_price) OVER (PARTITION BY p.category ORDER BY sale_date) as cumulative_category_sales,
        RANK() OVER (PARTITION BY p.category ORDER BY total_price DESC) as category_price_rank
    FROM sales s
    JOIN products p ON s.product_id = p.id
''').fetchall()

print(result)