# Generated: 2025-03-16 22:07:07.926362
# Result: [(1, datetime.date(2023, 1, 15), 10, Decimal('50.00'), 10, 50.0), (1, datetime.date(2023, 2, 20), 15, Decimal('52.50'), 25, 51.25), (2, datetime.date(2023, 1, 10), 5, Decimal('75.00'), 5, 75.0), (2, datetime.date(2023, 3, 5), 8, Decimal('77.25'), 13, 76.125)]
# Valid: True
import duckdb

# Create a connection
con = duckdb.connect(':memory:')

# Create a relation
rel = con.query('''SELECT * FROM (VALUES (1, 'Electronics', 500.50), (2, 'Clothing', 250.75)) AS sales(product_id, category, revenue)''')

# Explore relation properties
print('Columns:', rel.columns)
print('Types:', rel.types)
print('Number of rows:', len(rel.fetchall()))