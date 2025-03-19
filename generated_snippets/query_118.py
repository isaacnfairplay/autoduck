# Generated: 2025-03-19 17:50:28.800396
# Result: [(1, []), (2, [5, 6]), (3, [7, 8, 9])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with nested array data
conn.execute('''
CREATE TABLE nested_data (
    id INTEGER,
    nested_numbers INTEGER[]
)''')

# Insert sample nested array data
conn.executemany('INSERT INTO nested_data VALUES (?, ?)', [
    (1, [1, 2, 3]),
    (2, [4, 5, 6]),
    (3, [7, 8, 9])
])

# Use array_filter to extract numbers greater than 4
result = conn.execute('''
SELECT 
    id, 
    array_filter(nested_numbers, x -> x > 4) AS filtered_numbers
FROM nested_data
''').fetchall()

for row in result:
    print(row)