# Generated: 2025-03-19 13:17:36.777805
# Result: [('South', 'Gadget', Decimal('7500.000')), ('West', 'Gadget', Decimal('6100.000')), ('East', 'Widget', Decimal('3200.000')), ('North', 'Widget', Decimal('5000.000'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create geographic sales table
conn.execute('CREATE TABLE geo_sales (region TEXT, product TEXT, sales_amount DECIMAL)')
conn.execute('''INSERT INTO geo_sales VALUES
    ('North', 'Widget', 5000),
    ('South', 'Gadget', 7500),
    ('East', 'Widget', 3200),
    ('West', 'Gadget', 6100)''')

# Demonstrate QUALIFY window function with ranking
result = conn.execute('''
SELECT region, product, sales_amount
FROM (
    SELECT *,
    RANK() OVER (PARTITION BY region ORDER BY sales_amount DESC) as sales_rank
    FROM geo_sales
) ranked_sales
WHERE sales_rank = 1
''').fetchall()

for row in result:
    print(row)