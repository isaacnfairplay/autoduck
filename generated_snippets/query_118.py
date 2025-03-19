# Generated: 2025-03-19 19:17:48.103297
# Result: [11, 12, 13, 14]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
rel = conn.sql('SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array')
print(rel.execute().fetchall())