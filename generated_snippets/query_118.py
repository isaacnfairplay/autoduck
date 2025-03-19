# Generated: 2025-03-19 19:38:32.778333
# Result: [('Electronics', Decimal('48696.70'), 89.82666666666667), ('Sports', Decimal('11998.25'), 64.99)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE product_inventory (
    product_id INT,
    product_name VARCHAR,
    category VARCHAR,
    stock_quantity INT,
    unit_price DECIMAL(10,2)
);

INSERT INTO product_inventory VALUES
(1, 'Wireless Headphones', 'Electronics', 150, 79.99),
(2, 'Smart Speaker', 'Electronics', 200, 129.50),
(3, 'Running Shoes', 'Sports', 100, 89.99),
(4, 'Yoga Mat', 'Sports', 75, 39.99),
(5, 'Bluetooth Earbuds', 'Electronics', 180, 59.99);
''')

# Calculate total inventory value by category
result = conn.execute('''
SELECT 
    category, 
    SUM(stock_quantity * unit_price) as total_inventory_value,
    AVG(unit_price) as average_price
FROM product_inventory
GROUP BY category
ORDER BY total_inventory_value DESC
''').fetchall()

print(result)