# Generated: 2025-03-19 13:52:57.009599
# Result: [(1, True, 'Dell', 2), (2, True, 'Apple', 2)]
# Valid: True
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create table with complex nested data structure
conn.execute('''CREATE TABLE product_catalog (
    product_id INTEGER,
    tags VARCHAR[],
    metadata STRUCT(brand VARCHAR, specs VARCHAR[])
)''')

# Insert sample nested data
conn.execute('''INSERT INTO product_catalog VALUES
    (1, ['electronics', 'computer'], {'brand': 'Dell', 'specs': ['i7', '16GB']}),
    (2, ['electronics', 'smartphone'], {'brand': 'Apple', 'specs': ['A15', '128GB']})
''')

# Query nested structure using array and struct operations
result = conn.execute('''SELECT
    product_id,
    array_contains(tags, 'electronics') as is_electronics,
    metadata.brand as product_brand,
    array_length(metadata.specs) as spec_count
FROM product_catalog
''').fetchall()

print(result)