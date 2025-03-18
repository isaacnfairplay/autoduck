# Generated: 2025-03-16 23:56:18.109853
# Result: (102, 1, Decimal('750.25'), 750.25)
# Valid: True
import duckdb

con = duckdb.connect(':memory:')
rel = con.sql('SELECT * FROM (VALUES (1, 10), (2, 20), (3, 30)) AS t(id, value)')
agg_rel = rel.aggregate('SUM(value)')
print('Sum:', agg_rel.execute().fetchone()[0])