# Generated: 2025-03-19 12:34:38.909879
# Result: [(1, 'Electronics', 'Tech products'), (2, 'Clothing', 'Apparel and accessories'), (3, 'Home', 'Household items')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product category table
conn.execute('''
CREATE TABLE categories (
    category_id INT,
    name VARCHAR,
    description VARCHAR
);

INSERT INTO categories VALUES
    (1, 'Electronics', 'Tech products'),
    (2, 'Clothing', 'Apparel and accessories'),
    (3, 'Home', 'Household items');
'''
)

# Query to list all product categories
result = conn.execute('SELECT * FROM categories').fetchall()
for row in result:
    print(row)