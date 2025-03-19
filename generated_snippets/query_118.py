# Generated: 2025-03-19 16:59:03.777684
# Result: [('Clothing', 'Mens', Decimal('50.00'), 0), ('Clothing', 'Womens', Decimal('100.00'), 0), ('Clothing', None, Decimal('150.00'), 1), ('Electronics', 'Computers', Decimal('2700.00'), 0), ('Electronics', 'Phones', Decimal('800.00'), 0), ('Electronics', None, Decimal('3500.00'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample product sales table with hierarchical categories
conn.sql('''CREATE TABLE product_sales (
    category VARCHAR,
    subcategory VARCHAR,
    product VARCHAR,
    sales DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
    ('Electronics', 'Computers', 'Laptop', 1500.00),
    ('Electronics', 'Computers', 'Desktop', 1200.00),
    ('Electronics', 'Phones', 'Smartphone', 800.00),
    ('Clothing', 'Mens', 'Shirt', 50.00),
    ('Clothing', 'Womens', 'Dress', 100.00)
''');

# Compute total sales with nested grouping
result = conn.sql('''SELECT
    category,
    subcategory,
    SUM(sales) as total_sales,
    GROUPING(category, subcategory) as grouping_id
FROM product_sales
GROUP BY GROUPING SETS ((category), (category, subcategory))
ORDER BY category, subcategory
''').fetchall()

print(result)