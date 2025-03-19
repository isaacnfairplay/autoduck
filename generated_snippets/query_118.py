# Generated: 2025-03-19 10:13:17.454593
# Result: [(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 35)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate generating rows using VALUES clause
result = conn.execute('''
    SELECT * FROM (VALUES
        (1, 'Alice', 25),
        (2, 'Bob', 30),
        (3, 'Charlie', 35)
    ) AS people(id, name, age)
''').fetchall()

for row in result:
    print(row)