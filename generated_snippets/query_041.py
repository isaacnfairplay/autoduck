# Generated: 2025-03-16 22:41:27.491601
# Result: [('Engineering', 75000.0, 1), ('Sales', 52500.0, 2)]
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