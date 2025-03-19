# Generated: 2025-03-19 11:46:06.102817
# Result: [('Laptop', 'Electronics', 50, Decimal('1200.00'), Decimal('60000.00')), ('Smartphone', 'Electronics', 100, Decimal('800.50'), Decimal('140050.00')), ('Headphones', 'Electronics', 200, Decimal('150.25'), Decimal('170100.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
rel = conn.sql('SELECT 1 AS column')
print(rel.execute().fetchall())