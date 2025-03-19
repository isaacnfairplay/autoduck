# Generated: 2025-03-19 12:24:03.471662
# Result: [(1, 'Wireless Headphones', 'Electronics', Decimal('129.99'), Decimal('80.50'), datetime.date(2022, 11, 15), True, Decimal('38.07')), (2, 'Smart Watch', 'Wearables', Decimal('199.50'), Decimal('120.75'), datetime.date(2023, 1, 20), True, Decimal('39.47')), (3, 'Ergonomic Keyboard', 'Computer Accessories', Decimal('89.99'), Decimal('45.25'), datetime.date(2022, 9, 10), True, Decimal('49.72'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table with advanced attributes
conn.execute('''
CREATE TABLE product_sales (
    product_id INT PRIMARY KEY,
    product_name VARCHAR,
    category VARCHAR,
    list_price DECIMAL(10,2),
    cost_price DECIMAL(10,2),
    launch_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    profit_margin DECIMAL(5,2) GENERATED ALWAYS AS ((list_price - cost_price) / list_price * 100)
);

INSERT INTO product_sales (product_id, product_name, category, list_price, cost_price, launch_date) VALUES
    (1, 'Wireless Headphones', 'Electronics', 129.99, 80.50, '2022-11-15'),
    (2, 'Smart Watch', 'Wearables', 199.50, 120.75, '2023-01-20'),
    (3, 'Ergonomic Keyboard', 'Computer Accessories', 89.99, 45.25, '2022-09-10');
''')

# Verify table creation
result = conn.execute('SELECT * FROM product_sales').fetchall()
for row in result:
    print(row)