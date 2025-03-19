# Generated: 2025-03-19 17:45:57.008380
# Result: [([4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
rel = conn.sql('SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) as squared_array')
print(rel.execute().fetchall())