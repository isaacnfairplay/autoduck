# Generated: 2025-03-19 20:38:19.243068
# Result: [('Electronics', 'Phone', Decimal('800.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics table
conn.execute('CREATE TABLE electronics (category TEXT, product TEXT, price DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO electronics VALUES (?, ?, ?)', [
    ('Electronics', 'Phone', 800),
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Tablet', 500)
])

# Query specific product matching the task
result = conn.execute(
    "SELECT * FROM electronics WHERE category = 'Electronics' AND product = 'Phone' AND price = 800"
).fetchall()

print(result)