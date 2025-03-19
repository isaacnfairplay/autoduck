# Generated: 2025-03-19 13:43:13.391006
# Result: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE test_table (id INT, value VARCHAR)')
conn.executemany('INSERT INTO test_table VALUES (?, ?)', [(1, 'a'), (2, 'b'), (3, 'c')])

rel = conn.table('test_table').filter('id > 1')
print(rel.execute().fetchall())