# Generated: 2025-03-19 12:03:05.672160
# Result: [('Alice', 'USA', Decimal('350.75'))]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create users and purchases tables
conn.execute('CREATE TABLE users (user_id INT, name TEXT, country TEXT)')
conn.execute('CREATE TABLE purchases (purchase_id INT, user_id INT, amount DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO users VALUES (?, ?, ?)', [
    (1, 'Alice', 'USA'),
    (2, 'Bob', 'Canada'),
    (3, 'Charlie', 'UK')
])
conn.executemany('INSERT INTO purchases VALUES (?, ?, ?)', [
    (101, 1, 250.50),
    (102, 1, 100.25),
    (103, 2, 175.00)
])

# Demonstrate grouping and aggregation with join
result = conn.execute('''
    SELECT u.name, u.country, SUM(p.amount) as total_purchases
    FROM users u JOIN purchases p ON u.user_id = p.user_id
    GROUP BY u.name, u.country
    HAVING total_purchases > 200
''').fetchall()

print(result)