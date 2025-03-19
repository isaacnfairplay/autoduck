# Generated: 2025-03-19 08:58:21.543969
# Result: [(2,), (4,), (6,), (8,), (10,)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create example data
conn.execute('CREATE TABLE numbers (value INT)')
conn.executemany('INSERT INTO numbers VALUES (?)', [(x,) for x in range(1, 6)])

# Execute and print results
result = conn.execute('SELECT value * 2 as doubled FROM numbers').fetchall()
print(result)