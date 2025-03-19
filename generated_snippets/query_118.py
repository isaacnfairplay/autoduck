# Generated: 2025-03-19 13:06:43.394215
# Result: [('Widget', 'South', Decimal('800.000'), 2, Decimal('800.000')), ('Gadget', 'South', Decimal('1500.000'), 1, Decimal('2300.000')), ('Widget', 'North', Decimal('1000.000'), 2, Decimal('1000.000')), ('Gadget', 'North', Decimal('1200.000'), 1, Decimal('2200.000')), ('Widget', 'East', Decimal('1100.000'), 1, Decimal('1100.000'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create tables for demonstrating rank/window functions
conn.execute('CREATE TABLE sales (product TEXT, region TEXT, amount DECIMAL)')
conn.execute("""INSERT INTO sales VALUES
    ('Widget', 'North', 1000),
    ('Gadget', 'South', 1500),
    ('Widget', 'South', 800),
    ('Gadget', 'North', 1200),
    ('Widget', 'East', 1100)
""")

# Calculate cumulative sales and rank per region
result = conn.execute('''
    SELECT 
        product, 
        region, 
        amount,
        RANK() OVER (PARTITION BY region ORDER BY amount DESC) as sales_rank,
        SUM(amount) OVER (PARTITION BY region ORDER BY amount) as cumulative_sales
    FROM sales
''').fetchall()

for row in result:
    print(row)