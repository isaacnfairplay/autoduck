# Generated: 2025-03-19 19:49:46.818199
# Result: [('Laptop', Decimal('999.99'), datetime.date(2023, 1, 1), None), ('Laptop', Decimal('1099.99'), datetime.date(2023, 2, 1), Decimal('100.00')), ('Laptop', Decimal('949.99'), datetime.date(2023, 3, 1), Decimal('-150.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product price history table
conn.execute('''
CREATE TABLE product_prices (
    product_name VARCHAR,
    price DECIMAL(10,2),
    price_date DATE
);

INSERT INTO product_prices VALUES
('Laptop', 999.99, '2023-01-01'),
('Laptop', 1099.99, '2023-02-01'),
('Laptop', 949.99, '2023-03-01');
''')

# Calculate price changes with window functions
result = conn.execute('''
SELECT 
    product_name, 
    price, 
    price_date,
    price - LAG(price) OVER (PARTITION BY product_name ORDER BY price_date) as price_change
FROM product_prices
''').fetchall()

print(result)