# Generated: 2025-03-19 16:36:32.406389
# Result: [(1, [1, 2, 3], [2, 4, 6], [3]), (2, [4, 5, 6], [8, 10, 12], [4, 5, 6]), (3, [7, 8, 9], [14, 16, 18], [7, 8, 9])]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create array transformation example
conn.execute('CREATE TABLE arrays (id INTEGER, data INTEGER[])')
conn.executemany('INSERT INTO arrays VALUES (?, ?)', [
    (1, [1, 2, 3]),
    (2, [4, 5, 6]),
    (3, [7, 8, 9])
])

# Transform array using DuckDB functions
result = conn.execute('''
    SELECT 
        id, 
        data, 
        array_transform(data, x -> x * 2) as doubled_data,
        array_filter(data, x -> x > 2) as filtered_data
    FROM arrays
''').fetchall()

print(result)