# Generated: 2025-03-19 12:24:54.054667
# Result: [(1, 'Alice', 30), (2, 'Bob', 25), (3, 'Charlie', 35)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Table from VALUES clause demonstrating flexible data generation
result = conn.execute('''
SELECT * FROM (VALUES
    (1, 'Alice', 30),
    (2, 'Bob', 25),
    (3, 'Charlie', 35)
) AS people(id, name, age)
''').fetchall()

for row in result:
    print(row)