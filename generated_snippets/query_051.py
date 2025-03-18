# Generated: 2025-03-16 22:43:53.676461
# Result: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
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

# Filter rows using relation method
filtered_rel = rel.filter('price > 600')

print('High-Priced Products:')
for product in filtered_rel.execute().fetchall():
    print(product)