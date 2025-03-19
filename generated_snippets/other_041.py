# Generated: 2025-03-19 15:21:54.470085
# Result: [('banana', Decimal('200.75'), Decimal('150.30')), ('apple', Decimal('100.50'), Decimal('75.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE users (id INT, name VARCHAR, age INT)')
conn.execute("INSERT INTO users VALUES (1, 'Alice', 30), (2, 'Bob', 25), (3, 'Charlie', 35)")

rel = conn.table('users').filter('age > 25').order('age')
print(rel.execute().fetchall())