# Generated: 2025-03-19 17:23:59.430356
# Result: [('Gadget', 'South', Decimal('1500.00'), Decimal('2300.00'), 1), ('Gadget', 'South', Decimal('800.00'), Decimal('2300.00'), 2), ('Widget', 'North', Decimal('1200.00'), Decimal('2200.00'), 1), ('Widget', 'North', Decimal('1000.00'), Decimal('2200.00'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate advanced window function with multiple calculations
conn.execute('''
    CREATE TABLE sales (
        product TEXT,
        region TEXT,
        amount DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        ('Widget', 'North', 1000),
        ('Gadget', 'South', 1500),
        ('Widget', 'North', 1200),
        ('Gadget', 'South', 800);

    SELECT 
        product, 
        region, 
        amount,
        SUM(amount) OVER (PARTITION BY product) as total_product_sales,
        RANK() OVER (PARTITION BY region ORDER BY amount DESC) as sales_rank
    FROM sales;
''')

result = conn.fetchall()
for row in result:
    print(row)