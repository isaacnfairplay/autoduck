# Generated: 2025-03-19 13:28:43.366262
# Result: [1, 4, 9, 16]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE users (id INT, name STRING, age INT)')
conn.execute("INSERT INTO users VALUES (1, 'Alice', 30), (2, 'Bob', 25), (3, 'Charlie', 35)")

rel = conn.table('users').filter('age > 25')
print(rel.execute().fetchall())