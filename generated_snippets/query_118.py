# Generated: 2025-03-19 08:04:55.026005
# Result: [('Clothing', 'Jacket', Decimal('250.75'), Decimal('400.75'), 1), ('Clothing', 'Shoes', Decimal('150.00'), Decimal('150.00'), 2), ('Electronics', 'Laptop', Decimal('1200.50'), Decimal('2500.75'), 1), ('Electronics', 'Smartphone', Decimal('800.25'), Decimal('1300.25'), 2), ('Electronics', 'Tablet', Decimal('500.00'), Decimal('500.00'), 3)]
# Valid: True
import duckdb

# Create an in-memory database
conn = duckdb.connect(':memory:')

# Create a sample sales dataset
conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES 
    ('Electronics', 'Laptop', 1200.50),
    ('Electronics', 'Smartphone', 800.25),
    ('Clothing', 'Jacket', 250.75),
    ('Clothing', 'Shoes', 150.00),
    ('Electronics', 'Tablet', 500.00);
''')

# Window function analysis: cumulative sales and product ranking within category
result = conn.execute('''
SELECT 
    category, 
    product, 
    sales_amount,
    SUM(sales_amount) OVER (PARTITION BY category ORDER BY sales_amount) as cumulative_category_sales,
    RANK() OVER (PARTITION BY category ORDER BY sales_amount DESC) as product_rank
FROM product_sales
ORDER BY category, product_rank
''').fetchall()

for row in result:
    print(row)