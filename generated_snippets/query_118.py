# Generated: 2025-03-19 11:40:46.756405
# Result: [('Electronics', Decimal('140050.00'), 1000.25), ('Sports', Decimal('9000.00'), 120.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product inventory table
conn.execute('''
CREATE TABLE products (
    product_id INTEGER,
    name VARCHAR,
    category VARCHAR,
    stock_quantity INTEGER,
    unit_price DECIMAL(10,2)
);

INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 50, 1200.00),
(2, 'Smartphone', 'Electronics', 100, 800.50),
(3, 'Running Shoes', 'Sports', 75, 120.00);
''')

# Analyze inventory valuation by category
result = conn.execute('''
SELECT
    category,
    SUM(stock_quantity * unit_price) as total_inventory_value,
    AVG(unit_price) as avg_product_price
FROM products
GROUP BY category
ORDER BY total_inventory_value DESC
''').fetchall()

for row in result:
    print(f"{row[0]}: Inventory Value ${row[1]:.2f}, Avg Price ${row[2]:.2f}")