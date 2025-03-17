# Generated: 2025-03-16 22:44:11.272570
# Result: [(['name', 'price'],), (['name', 'price'],)]
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

# Method chaining: filter and project high-priced products
result = (rel
    .filter('price > 600')
    .project(['name', 'price'])
    .execute()
    .fetchall())

print('High-Priced Products:')
for product in result:
    print(product)