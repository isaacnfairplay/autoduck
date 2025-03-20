# Generated: 2025-03-19 20:40:50.721298
# Result: [('Clothing', 'Pants', Decimal('100.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create clothing table
conn.execute('CREATE TABLE clothing (category TEXT, product TEXT, price DECIMAL(10,2))')

# Insert sample data for Pants
conn.executemany('INSERT INTO clothing VALUES (?, ?, ?)', [
    ('Clothing', 'Pants', 100.00)
])

# Query for Pants with matching criteria
result = conn.execute(
    "SELECT * FROM clothing WHERE category = 'Clothing' AND product = 'Pants' AND price = 100.00"
).fetchall()

print(result)