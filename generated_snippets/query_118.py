# Generated: 2025-03-19 16:25:52.358765
# Result: [('Laptop', 'South', Decimal('1500.000'), Decimal('3600.000'), 1), ('Phone', 'South', Decimal('1200.000'), Decimal('2100.000'), 2), ('Tablet', 'South', Decimal('900.000'), Decimal('900.000'), 3), ('Laptop', 'North', Decimal('1000.000'), Decimal('2400.000'), 1), ('Phone', 'North', Decimal('800.000'), Decimal('1400.000'), 2), ('Tablet', 'North', Decimal('600.000'), Decimal('600.000'), 3)]
# Valid: True
import duckdb

# Create a connection
conn = duckdb.connect(':memory:')

# Create sample sales data with window functions
conn.execute('''
CREATE TABLE sales (
    product VARCHAR,
    region VARCHAR,
    sales_amount DECIMAL
);

INSERT INTO sales VALUES
    ('Laptop', 'North', 1000),
    ('Laptop', 'South', 1500),
    ('Phone', 'North', 800),
    ('Phone', 'South', 1200),
    ('Tablet', 'North', 600),
    ('Tablet', 'South', 900);
''')

# Calculate cumulative sales and rank products within each region
result = conn.execute('''
SELECT 
    product, 
    region, 
    sales_amount,
    SUM(sales_amount) OVER (PARTITION BY region ORDER BY sales_amount) as cumulative_sales,
    RANK() OVER (PARTITION BY region ORDER BY sales_amount DESC) as product_rank
FROM sales
''').fetchall()

for row in result:
    print(row)
