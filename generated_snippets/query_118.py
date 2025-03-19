# Generated: 2025-03-19 08:43:44.979419
# Result: [('Apple', 5, Decimal('1.50')), ('Banana', 3, Decimal('0.75')), ('Orange', 7, Decimal('1.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate table using VALUES clause
result = conn.execute("""
SELECT * FROM (VALUES
    ('Apple', 5, 1.50),
    ('Banana', 3, 0.75),
    ('Orange', 7, 1.25)
) AS fruits(name, quantity, price)
""").fetchall()

for row in result:
    print(f"Fruit: {row[0]}, Quantity: {row[1]}, Price: ${row[2]}")