# Generated: 2025-03-19 21:25:10.781861
# Result: [('"Alice"', '["Python","SQL"]', 2), ('"Bob"', '["Java","C++"]', 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE users (id INT, name VARCHAR, age INT)')
conn.execute("INSERT INTO users VALUES (1, 'Alice', 30), (2, 'Bob', 25), (3, 'Charlie', 35)")

rel = conn.table('users').filter('age > 25')
print(rel.execute().fetchall())