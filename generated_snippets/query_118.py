# Generated: 2025-03-19 12:20:31.692286
# Result: [('North', 'Laptop', Decimal('50000.00')), ('North', 'Tablet', Decimal('25000.00')), ('North', None, Decimal('75000.00')), ('South', 'Laptop', Decimal('45000.00')), ('South', 'Smartphone', Decimal('60000.00')), ('South', None, Decimal('105000.00')), (None, None, Decimal('180000.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create geographic sales data table
conn.execute('''
CREATE TABLE regional_sales (
    region VARCHAR,
    product VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO regional_sales VALUES
    ('North', 'Laptop', 50000.00),
    ('North', 'Tablet', 25000.00),
    ('South', 'Laptop', 45000.00),
    ('South', 'Smartphone', 60000.00);
'''
)

# Perform complex ROLLUP aggregation
result = conn.execute('''
SELECT 
    region, 
    product, 
    SUM(sales_amount) as total_sales
FROM regional_sales
GROUP BY ROLLUP(region, product)
ORDER BY region, product
''').fetchall()

for row in result:
    print(row)