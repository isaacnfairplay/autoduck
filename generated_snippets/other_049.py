# Generated: 2025-03-19 18:16:12.312310
# Result: [('Brazil', 'South America', 212559417), ('China', 'Asia', 1439323776), ('USA', 'North America', 331000000)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
rel = conn.table('duckdb_tables')
print(rel.execute().fetchall())