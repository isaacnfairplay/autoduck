# Generated: 2025-03-19 12:55:27.773615
# Result: [('Electronics', 2, Decimal('2000.75'), 1000.375), ('Furniture', 1, Decimal('250.75'), 250.75), ('Clothing', 1, Decimal('50.00'), 50.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE retail_sales AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200.50, '2023-01-15'),
    ('Electronics', 'Smartphone', 800.25, '2023-02-20'),
    ('Clothing', 'Shirt', 50.00, '2023-03-10'),
    ('Furniture', 'Chair', 250.75, '2023-04-05')
) AS t(category, product, amount, sale_date);
''')

# Aggregate sales by category with multi-column analysis
result = conn.execute('''
SELECT 
    category, 
    COUNT(*) as transaction_count,
    SUM(amount) as total_revenue,
    AVG(amount) as average_transaction
FROM retail_sales
GROUP BY category
ORDER BY total_revenue DESC
''').fetchall()

for row in result:
    print(row)