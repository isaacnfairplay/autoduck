# Generated: 2025-03-19 10:20:04.369039
# Result: [('South', 'Smartphone', Decimal('35000.00'), 1), ('West', 'Laptop', Decimal('45000.00'), 1), ('North', 'Laptop', Decimal('50000.00'), 1), ('East', 'Tablet', Decimal('25000.00'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create geographic sales data with product and region
conn.execute('''
    CREATE TABLE regional_sales (
        region VARCHAR,
        product VARCHAR,
        sales_amount DECIMAL(10,2)
    );

    INSERT INTO regional_sales VALUES
        ('North', 'Laptop', 50000.00),
        ('South', 'Smartphone', 35000.00),
        ('East', 'Tablet', 25000.00),
        ('West', 'Laptop', 45000.00)
''');

# Analyze sales by region with ranking
result = conn.execute('''
    SELECT 
        region, 
        product, 
        sales_amount,
        RANK() OVER (PARTITION BY region ORDER BY sales_amount DESC) as sales_rank
    FROM regional_sales
''').fetchall()

for row in result:
    print(row)