# Generated: 2025-03-19 16:53:00.498015
# Result: [('Electronics', 2, 799.745, Decimal('999.99'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('CREATE TABLE products (id INT, name VARCHAR, category VARCHAR, price DECIMAL(10,2))')

conn.executemany('INSERT INTO products VALUES (?, ?, ?, ?)', [
    (1, 'Laptop', 'Electronics', 999.99),
    (2, 'Smartphone', 'Electronics', 599.50),
    (3, 'Headphones', 'Accessories', 199.99)
])

# Complex aggregation and filtering across categories
result = conn.execute('''
    SELECT 
        category, 
        COUNT(*) as product_count,
        AVG(price) as avg_price,
        MAX(price) as max_price
    FROM products
    WHERE price > 500
    GROUP BY category
    HAVING COUNT(*) > 0
    ORDER BY avg_price DESC
''').fetchall()

print(result)