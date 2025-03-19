# Generated: 2025-03-19 08:44:35.676627
# Result: [('Electronics', 'Laptop', Decimal('1200.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics sales table
conn.execute('CREATE TABLE electronics_sales (category TEXT, product TEXT, price DECIMAL(10,2))')

# Insert specific sales data
conn.execute("INSERT INTO electronics_sales VALUES ('Electronics', 'Laptop', 1200)")

# Query and demonstrate result processing
result = conn.execute('SELECT * FROM electronics_sales WHERE category = ?', ['Electronics']).fetchall()

for row in result:
    print(f"Category: {row[0]}, Product: {row[1]}, Price: ${row[2]}")