# Generated: 2025-03-19 20:48:31.701280
# Result: [('Electronics', Decimal('2001.25')), ('Clothing', Decimal('200.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

print(conn.sql('SELECT 1').execute().fetchall())