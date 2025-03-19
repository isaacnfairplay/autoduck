# Generated: 2025-03-19 12:05:41.034711
# Result: [('Alice', 30), ('Charlie', 35)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE users (id INT, name TEXT, age INT)')
conn.executemany('INSERT INTO users VALUES (?, ?, ?)', [(1, 'Alice', 30), (2, 'Bob', 25), (3, 'Charlie', 35)])

result = conn.execute('SELECT name, age FROM users WHERE age > 28').fetchall()
print(result)