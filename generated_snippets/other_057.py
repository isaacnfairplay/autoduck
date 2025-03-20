# Generated: 2025-03-19 20:59:53.247460
# Result: [('Hello World', 'HELLO WORLD', 11, 'Hell0 W0rld'), ('DuckDB Rocks', 'DUCKDB ROCKS', 12, 'DuckDB R0cks'), ('SQL Processing', 'SQL PROCESSING', 14, 'SQL Pr0cessing')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.sql('CREATE TABLE numbers (value INTEGER)')
conn.sql('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

rel = conn.table('numbers').filter('value > 2')
print(rel.execute().fetchall())