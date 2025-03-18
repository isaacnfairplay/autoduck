# Generated: 2025-03-16 22:43:09.012378
# Result: [('Laptop',), ('Smartphone',), ('Tablet',)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Project only the name column
name_rel = rel.project('name')

result = name_rel.execute().fetchall()
print('Projected Names:', result)