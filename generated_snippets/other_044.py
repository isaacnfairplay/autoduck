# Generated: 2025-03-19 16:31:58.846637
# Result: [(0,), (1,), (1,), (2,), (3,), (5,), (8,), (13,), (21,), (34,)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE users (id INTEGER, name VARCHAR)')
conn.execute("INSERT INTO users VALUES (1, 'Alice'), (2, 'Bob')")
rel = conn.table('users').filter('id > 0')
print(rel.execute().fetchall())