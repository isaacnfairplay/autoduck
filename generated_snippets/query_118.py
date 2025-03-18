# Generated: 2025-03-18 16:20:09.709279
# Result: [('Electronics', 7.666666666666667, 0)]
# Valid: True
import duckdb

# Connect to in-memory database
con = duckdb.connect(':memory:')

# Create products table
con.execute('''
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    category VARCHAR,
    min_quantity INTEGER
);
''')

# Insert product data
con.executemany('INSERT INTO products VALUES (?, ?, ?, ?)', [
    (1, 'Laptop', 'Electronics', 10),
    (2, 'Smartphone', 'Electronics', 5),
    (3, 'Tablet', 'Electronics', 8)
])

# Create sales table with generated quantities
con.execute('''
CREATE TABLE sales AS
SELECT
    id AS product_id,
    name,
    category,
    min_quantity,
    GREATEST(min_quantity, (RANDOM() * 20)::INTEGER) AS actual_quantity
FROM products;
''')

# Analyze sales quantities relative to minimum
result = con.execute('''
SELECT
    category,
    AVG(actual_quantity) as avg_quantity,
    SUM(CASE WHEN actual_quantity > min_quantity THEN 1 ELSE 0 END) as exceeded_min_count
FROM sales
GROUP BY category
''').fetchall()

print(result)