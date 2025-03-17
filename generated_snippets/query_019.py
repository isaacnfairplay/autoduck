# Generated: 2025-03-16 22:12:08.532601
# Result: [(1, 'Electronics', Decimal('500.00'), 10), (3, 'Home Goods', Decimal('350.00'), 7)]
# Valid: True
import duckdb

# Connect to in-memory database
con = duckdb.connect(':memory:')

# Create sample relation
product_rel = con.sql('''SELECT * FROM (VALUES
    (1, 'Electronics', 500.00),
    (2, 'Clothing', 250.00),
    (3, 'Home Goods', 350.00)
) AS t(product_id, category, price)''')

# Filter relation and print result
filtered_rel = product_rel.filter('price > 300')
print('Filtered Relation:', filtered_rel.execute().fetchall())