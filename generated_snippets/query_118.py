# Generated: 2025-03-19 15:22:46.622786
# Result: [(1, 'Laptop', '16'), (2, 'Phone', '8')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with JSON column and parse complex nested data
conn.execute('CREATE TABLE products (id INT, details JSON)')
conn.execute("""INSERT INTO products VALUES
    (1, '{"name": "Laptop", "specs": {"ram": 16, "storage": "512GB SSD"}}'),
    (2, '{"name": "Phone", "specs": {"ram": 8, "storage": "256GB"}}')""")

# Extract and transform JSON data using SQL
result = conn.execute('''
    SELECT 
        id, 
        details->>'name' as product_name,
        details->'specs'->>'ram' as ram_size
    FROM products
    WHERE CAST(details->'specs'->>'ram' AS INT) >= 8
''').fetchall()

print(result)