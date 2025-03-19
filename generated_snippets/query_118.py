# Generated: 2025-03-19 09:07:09.438488
# Result: [(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 35)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table using VALUES directly
result = conn.execute('''SELECT * FROM (VALUES 
    (1, 'Alice', 25),
    (2, 'Bob', 30),
    (3, 'Charlie', 35)
) AS people(id, name, age)''').fetchall()

for row in result:
    print(f'ID: {row[0]}, Name: {row[1]}, Age: {row[2]}')