# Generated: 2025-03-19 13:34:47.451606
# Result: [('Charlie', 35, 1), ('Alice', 30, 2), ('Bob', 25, 3)]
# Valid: True
import duckdb

# Create an in-memory database and table
conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE users (id INT, name VARCHAR, age INT)')

# Insert sample data
conn.executemany('INSERT INTO users VALUES (?, ?, ?)', [
    (1, 'Alice', 30),
    (2, 'Bob', 25),
    (3, 'Charlie', 35)
])

# Perform a window function to rank users by age
result = conn.execute('''
    SELECT 
        name, 
        age, 
        RANK() OVER (ORDER BY age DESC) as age_rank
    FROM users
''').fetchall()

print(result)