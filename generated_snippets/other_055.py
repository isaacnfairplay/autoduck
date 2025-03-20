# Generated: 2025-03-19 20:13:11.638294
# Result: [('Laptop', 50, Decimal('999.99'), Decimal('49999.50'), Decimal('136198.75')), ('Smartphone', 100, Decimal('599.50'), Decimal('59950.00'), Decimal('136198.75')), ('Tablet', 75, Decimal('349.99'), Decimal('26249.25'), Decimal('136198.75'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE numbers (n INTEGER)')
conn.execute('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

rel = conn.table('numbers').filter('n > 2').project('n * 2 as doubled')
print(rel.execute().fetchall())