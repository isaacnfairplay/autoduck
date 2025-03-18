# Generated: 2025-03-16 22:41:12.286704
# Result: [('Engineering', 75000.0, 1), ('Sales', 52500.0, 2)]
# Valid: True
# Variable product: Type: tuple
# Attributes/Methods: count, index
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Filter products by price using relation method
filtered_rel = rel.filter('price > 600')

print('High-Priced Products:')
for product in filtered_rel.execute().fetchall():
    print(product)