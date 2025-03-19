# Generated: 2025-03-19 19:59:18.238076
# Result: [(1, [1, 2, 3], [1, 4, 9]), (2, [4, 5, 6], [16, 25, 36]), (3, [7, 8, 9], [49, 64, 81])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create array transformation example
conn.execute('CREATE TABLE arrays (id INT, numbers INTEGER[])')
conn.executemany('INSERT INTO arrays VALUES (?, ?)', [
    [1, [1, 2, 3]],
    [2, [4, 5, 6]],
    [3, [7, 8, 9]]
])

# Transform array: map each array element by squaring
result = conn.execute('''
    SELECT 
        id, 
        numbers, 
        array_transform(numbers, x -> x * x) as squared_numbers
    FROM arrays
''').fetchall()

for row in result:
    print(row)