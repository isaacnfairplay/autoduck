# Generated: 2025-03-19 14:17:20.507892
# Result: [('laptop', 45, 20), ('phone', 25, 12), ('tablet', 27, 11)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE numbers (n INTEGER)')
conn.execute('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

rel = conn.table('numbers').filter('n > 2').order('n').project('n * 2 as doubled')
print(rel.execute().fetchall())