# Generated: 2025-03-19 15:16:00.743847
# Result: [('bananas', Decimal('75.25'), Decimal('75.25')), ('bananas', Decimal('150.30'), Decimal('225.55')), ('apples', Decimal('100.50'), Decimal('100.50')), ('apples', Decimal('200.75'), Decimal('301.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate window functions with cumulative aggregation
conn.execute('CREATE TABLE sales (product TEXT, amount DECIMAL(10,2))')
conn.execute("INSERT INTO sales VALUES ('apples', 100.50), ('bananas', 75.25), ('apples', 200.75), ('bananas', 150.30)")

result = conn.execute('''
    SELECT 
        product, 
        amount, 
        SUM(amount) OVER (PARTITION BY product ORDER BY amount) as cumulative_sales
    FROM sales
''').fetchall()

print(result)