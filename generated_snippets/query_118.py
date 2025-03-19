# Generated: 2025-03-19 14:16:29.989535
# Result: [('laptop', 45, 20), ('phone', 25, 12), ('tablet', 27, 11)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with product inventory and use LIST_AGGREGATE to compute total quantities
conn.execute('CREATE TABLE inventory (product TEXT, quantities INTEGER[])')
conn.execute("""INSERT INTO inventory VALUES
    ('laptop', [10, 15, 20]),
    ('phone', [5, 8, 12]),
    ('tablet', [7, 9, 11])
""")

result = conn.execute('''
    SELECT product, 
           LIST_AGGREGATE(quantities, 'sum') as total_quantity,
           LIST_AGGREGATE(quantities, 'max') as max_quantity
    FROM inventory
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Total Quantity: {row[1]}, Max Quantity: {row[2]}")