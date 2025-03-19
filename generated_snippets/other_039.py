# Generated: 2025-03-19 14:50:56.827082
# Result: [(1, 'Alice', [90, 95, 100])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE numbers (value INTEGER)')
conn.execute('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

rel = conn.table('numbers').filter('value > 2').project('value * 2 AS doubled_value')
print(rel.execute().fetchall())