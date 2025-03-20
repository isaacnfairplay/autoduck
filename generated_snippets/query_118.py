# Generated: 2025-03-19 20:39:09.428135
# Result: [('Electronics', 'Tablet', Decimal('500.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics table
conn.execute('CREATE TABLE electronics (category TEXT, product TEXT, price DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO electronics VALUES (?, ?, ?)', [
    ('Electronics', 'Tablet', 500)
])

# Query for Tablet with matching criteria
result = conn.execute(
    "SELECT * FROM electronics WHERE category = 'Electronics' AND product = 'Tablet' AND price = 500"
).fetchall()

print(result)