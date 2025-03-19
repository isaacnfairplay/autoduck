# Generated: 2025-03-19 18:29:41.534500
# Result: [('"Alice"', '30')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

rel = conn.sql('SELECT * FROM (VALUES (1, 2), (3, 4), (5, 6)) AS t(a, b)')
print(rel.execute().fetchall())