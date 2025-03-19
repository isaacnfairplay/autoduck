# Generated: 2025-03-19 18:41:53.600955
# Result: 5.0
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample table
conn.execute('CREATE TABLE numbers (val INTEGER)')
conn.execute('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

# Create relational query
rel = conn.table('numbers').filter('val > 2')
print(rel.execute().fetchall())