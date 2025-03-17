# Generated: 2025-03-16 22:08:49.290242
# Result: ('Books', 1, Decimal('100.25'), 100.25)
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a sample relation of product sales
rel = con.query('''
SELECT * FROM (VALUES 
    (1, 'Electronics', 500.50, '2023-01-15'),
    (2, 'Clothing', 250.75, '2023-02-20'),
    (3, 'Books', 100.25, '2023-03-10')
) AS sales(product_id, category, revenue, sale_date)
''')

# Filter the relation to get high-revenue products
filtered_rel = rel.filter('revenue > 200.0')

# Display filtered results
print('High Revenue Products:', filtered_rel.execute().fetchall())