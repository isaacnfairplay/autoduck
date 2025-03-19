# Generated: 2025-03-19 15:21:04.207121
# Result: [('banana', Decimal('200.75'), Decimal('150.30')), ('apple', Decimal('100.50'), Decimal('75.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Cross tabulation with multiple aggregation strategies
conn.execute('CREATE TABLE sales (product TEXT, region TEXT, amount DECIMAL(10,2))')
conn.execute("""INSERT INTO sales VALUES
    ('apple', 'North', 100.50),
    ('apple', 'South', 75.25),
    ('banana', 'North', 200.75),
    ('banana', 'South', 150.30)
""")

result = conn.execute('''
    PIVOT sales
    ON region
    USING SUM(amount)
    GROUP BY product
''').fetchall()

print(result)  # Demonstrates cross-tabulation of sales by product and region