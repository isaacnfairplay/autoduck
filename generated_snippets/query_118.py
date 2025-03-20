# Generated: 2025-03-19 20:40:00.001282
# Result: [('Clothing', 'Shirt', Decimal('50.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create clothing table
conn.execute('CREATE TABLE clothing (category TEXT, product TEXT, price DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO clothing VALUES (?, ?, ?)', [
    ('Clothing', 'Shirt', 50.00)
])

# Query for Shirt with matching criteria
result = conn.execute(
    "SELECT * FROM clothing WHERE category = 'Clothing' AND product = 'Shirt' AND price = 50.00"
).fetchall()

print(result)