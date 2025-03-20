# Generated: 2025-03-19 20:37:27.961177
# Result: [('Electronics', 'Laptop', Decimal('1200.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics table
conn.execute('CREATE TABLE electronics (category TEXT, product TEXT, price DECIMAL(10,2))')

# Insert specific electronics data
conn.executemany('INSERT INTO electronics VALUES (?, ?, ?)', [
    ('Electronics', 'Laptop', 1200.00),
    ('Electronics', 'Smartphone', 800.50),
    ('Electronics', 'Tablet', 500.25)
])

# Query to match specific electronics item
result = conn.execute(
    "SELECT * FROM electronics WHERE category = 'Electronics' AND product = 'Laptop' AND price = 1200.00"
).fetchall()

print(result)