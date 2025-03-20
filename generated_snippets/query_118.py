# Generated: 2025-03-19 20:07:21.285411
# Result: [(1, [[2, 4], [6, 8]]), (2, [[10, 12], [14, 16]])]
# Valid: True
import duckdb

con = duckdb.connect(':memory:')

# Create a complex multi-dimensional array transformation example
con.execute('''
CREATE TABLE nested_data (
    id INTEGER,
    nested_array INTEGER[][]
);

INSERT INTO nested_data VALUES
    (1, [[1, 2], [3, 4]]),
    (2, [[5, 6], [7, 8]]);

SELECT 
    id, 
    array_transform(nested_array, x -> array_transform(x, y -> y * 2)) AS doubled_array
FROM nested_data;
'''
)

result = con.execute('''
SELECT 
    id, 
    array_transform(nested_array, x -> array_transform(x, y -> y * 2)) AS doubled_array
FROM nested_data;
''').fetchall()

for row in result:
    print(f"ID: {row[0]}, Transformed Array: {row[1]})")