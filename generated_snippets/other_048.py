# Generated: 2025-03-19 18:06:37.146586
# Result: [('New York', -74.006, 40.7128)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE numbers (value INTEGER)')
conn.execute('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

rel = conn.table('numbers').filter('value > 2').project('value * 2 AS doubled_value')