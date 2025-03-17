# Generated: 2025-03-16 22:52:41.435512
# Result: [(1, 'Alice'), (2, 'Bob')]
# Valid: True
import duckdb

con = duckdb.connect(':memory:')
con.execute('CREATE TABLE users (id INT, name VARCHAR)')
con.execute("INSERT INTO users VALUES (1, 'Alice'), (2, 'Bob')")

result = con.execute('SELECT * FROM users').fetchall()
print(result)