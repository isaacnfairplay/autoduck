# Generated: 2025-03-19 10:28:44.650793
# Result: [('Smartphone', 'Electronics', datetime.date(2023, 7, 2), 15, Decimal('18992.40'), 1), ('Laptop', 'Electronics', datetime.date(2023, 7, 1), 10, Decimal('9999.90'), 2), ('Desk Chair', 'Furniture', datetime.date(2023, 7, 3), 5, Decimal('1249.95'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample data
conn.execute('CREATE TABLE numbers (value INTEGER)')
conn.execute('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

# Create a relation and execute
rel = conn.table('numbers').filter('value > 2')
print(rel.execute().fetchall())