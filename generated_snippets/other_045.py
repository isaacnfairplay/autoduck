# Generated: 2025-03-19 17:08:21.575536
# Result: [([4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
rel = conn.table('sqlite_master')
print(rel.execute().fetchall())