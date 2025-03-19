# Generated: 2025-03-19 19:55:47.122610
# Result: [('Phone', 150, 40, 0.26666666666666666, 1), ('Laptop', 100, 25, 0.25, 2), ('Tablet', 75, 15, 0.2, 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('CREATE TABLE numbers (id INT, value INT)')
conn.execute('INSERT INTO numbers VALUES (1, 10), (2, 20), (3, 30)')

rel = conn.table('numbers').filter('value > 15')
print(rel.execute().fetchall())