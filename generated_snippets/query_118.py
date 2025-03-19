# Generated: 2025-03-19 14:44:50.711517
# Result: [('Apple', Decimal('0.50'), Decimal('0.50')), ('Orange', Decimal('0.60'), Decimal('1.10')), ('Banana', Decimal('0.75'), Decimal('1.85'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a temporary table of products
conn.execute("CREATE TABLE products (id INTEGER, name VARCHAR, price DECIMAL(10,2))")
conn.execute("INSERT INTO products VALUES (1, 'Apple', 0.50), (2, 'Banana', 0.75), (3, 'Orange', 0.60)")

# Use window function to calculate running total of prices
result = conn.execute("SELECT name, price, SUM(price) OVER (ORDER BY price) as running_total FROM products").fetchall()

for row in result:
    print(f"{row[0]}: Price ${row[1]}, Running Total ${row[2]})")