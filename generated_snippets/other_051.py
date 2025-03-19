# Generated: 2025-03-19 19:04:11.885823
# Result: [(3, 'Marketing', Decimal('85.70'), 0.0), (4, 'Marketing', Decimal('91.20'), 1.0), (1, 'Sales', Decimal('88.50'), 0.0), (2, 'Sales', Decimal('92.30'), 1.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample table
conn.sql('CREATE TABLE numbers (value INTEGER)')
conn.sql('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

# Use relational API to execute query
rel = conn.table('numbers').filter('value > 2')
print(rel.execute().fetchall())