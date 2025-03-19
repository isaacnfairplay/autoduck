# Generated: 2025-03-19 19:27:18.088095
# Result: [('Electronics', Decimal('14999.50'), 299.99), ('Clothing', Decimal('9749.40'), 64.745), ('Home', Decimal('9749.25'), 129.99)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample table
conn.execute('CREATE TABLE numbers (value INTEGER)')
conn.execute('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

# Create a relation and execute
rel = conn.table('numbers').filter('value > 2')
print(rel.execute().fetchall())