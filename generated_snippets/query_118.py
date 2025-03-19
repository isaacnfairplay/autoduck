# Generated: 2025-03-19 10:53:59.797490
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create sample sales data
conn.execute('''
    CREATE TABLE sales (
        product TEXT,
        region TEXT,
        sales_amount DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        ('Laptop', 'North', 5000.50),
        ('Phone', 'South', 3200.75),
        ('Tablet', 'East', 2100.25),
        ('Laptop', 'West', 4500.60)
''');

# Demonstrate window function: running total of sales by region
result = conn.execute('''
    SELECT 
        product, 
        region, 
        sales_amount,
        SUM(sales_amount) OVER (PARTITION BY region ORDER BY sales_amount) as running_total
    FROM sales
''').fetchall()

print(result)