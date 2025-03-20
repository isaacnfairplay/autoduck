# Generated: 2025-03-19 21:36:25.333835
# Result: [('C', 'D', Decimal('0.40'), Decimal('0.40')), ('B', 'D', Decimal('0.85'), Decimal('0.85')), ('A', 'B', Decimal('0.75'), Decimal('0.75')), ('A', 'C', Decimal('0.60'), Decimal('0.75')), ('D', 'E', Decimal('0.95'), Decimal('0.95'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
rel = conn.sql('SELECT 1 AS value')
print(rel.execute().fetchall())