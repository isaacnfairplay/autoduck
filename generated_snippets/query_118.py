# Generated: 2025-03-19 11:06:42.362935
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a product catalog with inventory tracking
conn.sql('''
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name VARCHAR,
    category VARCHAR,
    price DECIMAL(10,2)
);

CREATE TABLE inventory (
    product_id INTEGER,
    warehouse_id INTEGER,
    stock_quantity INTEGER
);

INSERT INTO products VALUES
    (1, 'Laptop', 'Electronics', 999.99),
    (2, 'Smartphone', 'Electronics', 599.99),
    (3, 'Desk Chair', 'Furniture', 249.99);

INSERT INTO inventory VALUES
    (1, 1, 50),
    (1, 2, 30),
    (2, 1, 75),
    (3, 2, 20);

-- Find total inventory and average price per category
SELECT 
    p.category,
    SUM(i.stock_quantity) as total_stock,
    AVG(p.price) as avg_category_price
FROM products p
JOIN inventory i ON p.product_id = i.product_id
GROUP BY p.category
''').show()
