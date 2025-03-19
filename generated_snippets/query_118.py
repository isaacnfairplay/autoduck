# Generated: 2025-03-19 14:02:42.978691
# Result: [(1, 'red', 'large'), (2, 'blue', 'medium')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with complex nested data
conn.execute('''
CREATE TABLE product_details (
    product_id INTEGER,
    features STRUCT(color VARCHAR, size VARCHAR, material VARCHAR)
);

INSERT INTO product_details VALUES
    (1, {'color': 'red', 'size': 'large', 'material': 'cotton'}),
    (2, {'color': 'blue', 'size': 'medium', 'material': 'polyester'});
''')

# Extract nested struct fields
result = conn.execute('''
SELECT 
    product_id, 
    features.color as product_color,
    features.size as product_size
FROM product_details
''').fetchall()

for row in result:
    print(row)