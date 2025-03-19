# Generated: 2025-03-19 13:21:08.014539
# Result: [('Gadget', 'South', Decimal('1500.75'), 1), ('Widget', 'South', Decimal('950.30'), 2), ('Gadget', 'West', Decimal('1200.60'), 1), ('Widget', 'North', Decimal('1000.50'), 1), ('Widget', 'East', Decimal('800.25'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Complex example: Window functions with conditional ranking
conn.execute('''CREATE TABLE sales (
    product TEXT,
    region TEXT,
    amount DECIMAL(10,2)
)''')

conn.execute('''INSERT INTO sales VALUES
    ('Widget', 'North', 1000.50),
    ('Gadget', 'South', 1500.75),
    ('Widget', 'East', 800.25),
    ('Gadget', 'West', 1200.60),
    ('Widget', 'South', 950.30)''')

# Rank products within each region by sales amount
result = conn.execute('''SELECT
    product,
    region,
    amount,
    RANK() OVER (PARTITION BY region ORDER BY amount DESC) as regional_rank
FROM sales
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Region: {row[1]}, Amount: ${row[2]}, Regional Rank: {row[3]}")