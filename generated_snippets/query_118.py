# Generated: 2025-03-19 08:11:54.232184
# Result: [('Apple', 10), ('Banana', 15), ('Cherry', 20)]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Generate table directly from VALUES clause
result = conn.execute('''
SELECT * FROM (VALUES
    ('Apple', 10),
    ('Banana', 15),
    ('Cherry', 20)
) AS fruits(name, quantity)
''').fetchall()

for row in result:
    print(row)