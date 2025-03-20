# Generated: 2025-03-19 20:09:34.551867
# Result: [(1, [11, 12, 13]), (2, [14, 15, 16])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE numeric_arrays (id INTEGER, values INTEGER[]);
INSERT INTO numeric_arrays VALUES
    (1, [1, 2, 3]),
    (2, [4, 5, 6]);
''')

result = conn.execute('''
SELECT
    id,
    array_transform(values, x -> x + 10) AS transformed_values
FROM numeric_arrays
''').fetchall()

for row in result:
    print(f"ID: {row[0]}, Transformed: {row[1]})")