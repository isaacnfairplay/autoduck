# Generated: 2025-03-19 08:27:02.755745
# Result: [('North', Decimal('50000.00'), 50000.0), ('South', Decimal('45000.00'), 45000.0), ('East', Decimal('30000.00'), 30000.0)]
# Valid: True
import duckdb

# Create an in-memory database
conn = duckdb.connect(':memory:')

# Create sales performance tracking table
conn.execute('''
CREATE TABLE sales_performance (
    product VARCHAR,
    region VARCHAR,
    sales_amount DECIMAL(10,2),
    sales_quarter VARCHAR
);

INSERT INTO sales_performance VALUES
    ('Laptop', 'North', 50000.00, 'Q2'),
    ('Smartphone', 'South', 45000.00, 'Q2'),
    ('Tablet', 'East', 30000.00, 'Q2');
'''
)

# Analyze regional sales performance
result = conn.execute('''
SELECT
    region,
    SUM(sales_amount) as total_regional_sales,
    AVG(sales_amount) as avg_product_sales
FROM sales_performance
GROUP BY region
ORDER BY total_regional_sales DESC
''').fetchall()

for row in result:
    print(row)