# Generated: 2025-03-19 14:09:40.515914
# Result: [('laptop', 'North', Decimal('1000.00'), Decimal('1000.00')), ('tablet', 'North', Decimal('800.00'), Decimal('1800.00')), ('laptop', 'South', Decimal('1200.00'), Decimal('1200.00')), ('phone', 'South', Decimal('1500.00'), Decimal('2700.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample table with sales data
conn.execute('CREATE TABLE sales (product TEXT, region TEXT, amount DECIMAL(10,2))')
conn.execute("INSERT INTO sales VALUES ('laptop', 'North', 1000), ('phone', 'South', 1500), ('tablet', 'North', 800), ('laptop', 'South', 1200)")

# Use window function to calculate running total per region
result = conn.execute('''
    SELECT product, region, amount,
           SUM(amount) OVER (PARTITION BY region ORDER BY product) as running_total
    FROM sales
    ORDER BY region, product
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Region: {row[1]}, Amount: {row[2]}, Running Total: {row[3]})")