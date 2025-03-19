# Generated: 2025-03-19 09:21:06.283563
# Result: [(6, 12), (7, 14), (8, 16), (9, 18), (10, 20)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample table
conn.execute('CREATE TABLE numbers (value INT)')
conn.executemany('INSERT INTO numbers VALUES (?)', [(x,) for x in range(1, 11)])

# Filter and transform data
result = conn.execute('SELECT value, value * 2 as doubled FROM numbers WHERE value > 5').fetchall()

for row in result:
    print(f'Original: {row[0]}, Doubled: {row[1]}')