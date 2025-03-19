# Generated: 2025-03-19 12:22:16.867833
# Result: [('Clothing', 1, Decimal('285.00'), 26.25), ('Electronics', 1, Decimal('407.50'), 51.25)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate product sales table
conn.execute('''
CREATE TABLE product_sales (
    product_id INT,
    category VARCHAR,
    sale_date DATE,
    quantity INT,
    price DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
    (1, 'Electronics', '2023-01-15', 5, 50.00),
    (1, 'Electronics', '2023-02-20', 3, 52.50),
    (2, 'Clothing', '2023-01-10', 7, 25.00),
    (2, 'Clothing', '2023-03-05', 4, 27.50);
''')

# Demonstrate analytical query with multiple aggregations
result = conn.execute('''
SELECT 
    category,
    COUNT(DISTINCT product_id) as unique_products,
    SUM(quantity * price) as total_revenue,
    AVG(price) as avg_price
FROM product_sales
GROUP BY category
''').fetchall()

for row in result:
    print(row)