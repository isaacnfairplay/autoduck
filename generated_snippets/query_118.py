# Generated: 2025-03-19 12:15:05.357115
# Result: [(2, 'Smartphone', Decimal('600.00'), Decimal('10.00'), 540.0), (1, 'Laptop', Decimal('1000.00'), Decimal('15.00'), 850.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create products and discounts tables
conn.execute('CREATE TABLE products(product_id INT, name TEXT, price DECIMAL(10,2))')
conn.execute('CREATE TABLE discount_rules(min_price DECIMAL(10,2), discount_percentage DECIMAL(5,2))')

conn.executemany('INSERT INTO products VALUES (?, ?, ?)', [
    (1, 'Laptop', 1000.00),
    (2, 'Smartphone', 600.00),
    (3, 'Tablet', 400.00)
])

conn.executemany('INSERT INTO discount_rules VALUES (?, ?)', [
    (500.00, 10.0),
    (1000.00, 15.0)
])

# Use LATERAL JOIN to dynamically apply discounts
result = conn.execute('''
    SELECT 
        p.product_id, 
        p.name, 
        p.price, 
        d.discount_percentage,
        p.price * (1 - d.discount_percentage/100) as discounted_price
    FROM products p, LATERAL (
        SELECT discount_percentage 
        FROM discount_rules 
        WHERE p.price >= min_price 
        ORDER BY discount_percentage DESC 
        LIMIT 1
    ) d
''').fetchall()

print(result)