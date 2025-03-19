# Generated: 2025-03-19 12:32:03.864329
# Result: [(1, 'Electronics', Decimal('50000.00'), 1, 47500.0), (2, 'Electronics', Decimal('45000.00'), 2, 47500.0), (4, 'Clothing', Decimal('35000.00'), 1, 32500.0), (3, 'Clothing', Decimal('30000.00'), 2, 32500.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE products (
    product_id INT,
    category VARCHAR,
    sales DECIMAL(10,2)
);

INSERT INTO products VALUES
    (1, 'Electronics', 50000),
    (2, 'Electronics', 45000),
    (3, 'Clothing', 30000),
    (4, 'Clothing', 35000);
''')

# Correlated subquery ranking products within category
result = conn.execute('''
SELECT
    product_id,
    category,
    sales,
    RANK() OVER (PARTITION BY category ORDER BY sales DESC) as category_rank,
    (SELECT AVG(sales) FROM products p2 WHERE p2.category = p1.category) as category_avg_sales
FROM products p1
''').fetchall()

for row in result:
    print(row)