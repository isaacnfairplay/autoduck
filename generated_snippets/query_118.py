# Generated: 2025-03-19 08:47:08.759240
# Result: [('Electronics', 'Laptop', Decimal('1200.50')), ('Electronics', 'Phone', Decimal('800.25')), ('Electronics', 'Tablet', Decimal('500.75'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table and insert multiple rows using VALUES clause
result = conn.execute("""
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200.50),
    ('Electronics', 'Phone', 800.25),
    ('Electronics', 'Tablet', 500.75)
) AS t(category, product, amount)
""").fetchall()

for row in result:
    print(f"Category: {row[0]}, Product: {row[1]}, Amount: ${row[2]:.2f}")