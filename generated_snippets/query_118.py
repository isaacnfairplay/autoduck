# Generated: 2025-03-19 11:31:04.754255
# Result: [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate direct VALUES usage in query
result = conn.execute("SELECT * FROM (VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')) AS names(id, name)").fetchall()

for row in result:
    print(f"ID: {row[0]}, Name: {row[1]}")