# Generated: 2025-03-16 22:43:17.024344
# Result: [('Laptop',), ('Smartphone',), ('Tablet',)]
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

# Demonstrate relation query methods
filtered_rel = rel.filter('price > 600')
transformed_rel = filtered_rel.project(['name', 'price'])

print('High-Priced Products:')
for product in transformed_rel.execute().fetchall():
    print(product)