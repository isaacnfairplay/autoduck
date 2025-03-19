# Generated: 2025-03-19 15:02:12.450458
# Result: <duckdb.duckdb.DuckDBPyConnection object at 0x00000147DE9344F0>
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample table and demonstrate complex aggregation
conn.execute('''CREATE TABLE products (category VARCHAR, price DECIMAL)''')
conn.execute('''INSERT INTO products VALUES
    ('Electronics', 500), ('Clothing', 100), 
    ('Electronics', 750), ('Clothing', 200),
    ('Electronics', 600)''')

rel = conn.sql('''
    SELECT 
        category, 
        COUNT(*) as product_count,
        AVG(price) as avg_price,
        MAX(price) - MIN(price) as price_range
    FROM products
    GROUP BY category
    HAVING COUNT(*) > 1
''')

print(rel.execute().fetchall())