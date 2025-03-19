# Generated: 2025-03-19 08:36:48.278755
# Result: [('Widget', 1, Decimal('1000.50'), Decimal('1000.50')), ('Widget', 2, Decimal('1200.25'), Decimal('2200.75')), ('Gadget', 1, Decimal('1500.75'), Decimal('1500.75')), ('Gadget', 2, Decimal('1750.60'), Decimal('3251.35'))]
# Valid: True
# Variable data: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data
conn.execute('CREATE TABLE sales (product TEXT, month INT, revenue DECIMAL(10,2))')
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('Widget', 1, 1000.50), ('Gadget', 1, 1500.75),
    ('Widget', 2, 1200.25), ('Gadget', 2, 1750.60)
])

# Calculate cumulative revenue per product using window function
result = conn.execute('''
    SELECT 
        product, 
        month, 
        revenue,
        SUM(revenue) OVER (PARTITION BY product ORDER BY month) as cumulative_revenue
    FROM sales
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Month: {row[1]}, Revenue: {row[2]}, Cumulative: {row[3]})")