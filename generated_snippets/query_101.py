# Generated: 2025-03-17 19:49:55.708661
# Result: [(1, 'Alice', 30), (3, 'Charlie', 35)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a sample table
con.execute('CREATE TABLE users (id INT, name VARCHAR, age INT)')

# Insert sample data
con.executemany('INSERT INTO users VALUES (?, ?, ?)', [
    (1, 'Alice', 30),
    (2, 'Bob', 25),
    (3, 'Charlie', 35)
])

# Execute a query and fetch results
result = con.execute('SELECT * FROM users WHERE age > 27').fetchall()
print(result)