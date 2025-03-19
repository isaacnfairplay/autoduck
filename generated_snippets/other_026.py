# Generated: 2025-03-19 09:52:41.809622
# Result: [('Electronics', 'Laptop', 1200), ('Electronics', 'Phone', 800)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
rel = conn.table('sqlite_master')
print(rel.execute().fetchall())