# Generated: 2025-03-19 21:14:45.169634
# Result: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
rel = conn.sql('SELECT range(10) AS numbers')
print(rel.execute().fetchall())