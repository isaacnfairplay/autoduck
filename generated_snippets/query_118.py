# Generated: 2025-03-19 10:49:20.159558
# Result: [('Engineering', 88500.0, Decimal('92000.00'), 2), ('Sales', 72000.0, Decimal('72000.00'), 1), ('Marketing', 65000.0, Decimal('65000.00'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
rel = conn.sql('SELECT 1 + 1 AS result')
print(rel.execute().fetchall())