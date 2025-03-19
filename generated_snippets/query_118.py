# Generated: 2025-03-19 19:26:28.136146
# Result: [('Electronics', Decimal('14999.50'), 299.99), ('Clothing', Decimal('9749.40'), 64.745), ('Home', Decimal('9749.25'), 129.99)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a product inventory with categories and perform conditional aggregation
conn.execute('''CREATE TABLE product_inventory (
    product_id INTEGER,
    category VARCHAR,
    stock_quantity INTEGER,
    unit_price DECIMAL(10,2)
)''')

conn.execute('''INSERT INTO product_inventory VALUES
    (1, 'Electronics', 50, 299.99),
    (2, 'Clothing', 100, 49.50),
    (3, 'Electronics', 25, 599.99),
    (4, 'Home', 75, 129.99),
    (5, 'Clothing', 60, 79.99)''')

# Compute total value and average price per category, with stock threshold filter
result = conn.execute('''SELECT 
    category, 
    SUM(stock_quantity * unit_price) as total_category_value,
    AVG(unit_price) as avg_price
FROM product_inventory
WHERE stock_quantity > 30
GROUP BY category
ORDER BY total_category_value DESC''').fetchall()

for row in result:
    print(f'Category: {row[0]}, Total Value: ${row[1]}, Avg Price: ${row[2]:.2f}')