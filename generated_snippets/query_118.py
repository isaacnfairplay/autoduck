# Generated: 2025-03-19 11:44:14.425053
# Result: [('Electronics', 1500), ('Electronics', 2300), ('Clothing', 1000), ('Clothing', 1750)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales data table
conn.execute('''
CREATE TABLE sales AS
SELECT 'Electronics' as category, 1500 as amount
UNION ALL
SELECT 'Electronics', 2300
UNION ALL
SELECT 'Clothing', 1000
UNION ALL
SELECT 'Clothing', 1750
''')

# Fetch and display sales data
result = conn.execute('SELECT * FROM sales').fetchall()
for row in result:
    print(f"Category: {row[0]}, Amount: {row[1]}")