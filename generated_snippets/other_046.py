# Generated: 2025-03-19 17:30:51.610467
# Result: [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE numbers (val INTEGER)')
conn.execute('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

rel = conn.table('numbers').filter('val > 2').project('val * 2 AS doubled_val')
print(rel.execute().fetchall())