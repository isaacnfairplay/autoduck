# Generated: 2025-03-16 22:42:42.579520
# Result: [(1, 2, 18, 25.5, Decimal('25.50')), (2, 1, 5, 30.75, Decimal('30.75'))]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Filter products with id greater than 1
filtered_rel = rel.filter('id > 1')

print('Filtered Results:', filtered_rel.execute().fetchall())