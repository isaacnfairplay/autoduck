# Generated: 2025-03-19 20:03:43.578415
# Result: [(1, [1, 4, 9]), (2, [16, 25, 36]), (3, [49, 64, 81])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with arrays and transform them
conn.execute('''
    CREATE TABLE numbers (id INTEGER, values INTEGER[]);
    INSERT INTO numbers VALUES
        (1, [1, 2, 3]),
        (2, [4, 5, 6]),
        (3, [7, 8, 9]);
''')

# Use array_transform to square each element
result = conn.execute('''
    SELECT 
        id, 
        array_transform(values, x -> x * x) AS squared_values
    FROM numbers
''').fetchall()

for row in result:
    print(f"ID: {row[0]}, Squared Values: {row[1]}")