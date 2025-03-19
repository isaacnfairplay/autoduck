# Generated: 2025-03-19 12:13:18.876757
# Result: [('New York', 10851.73306683613), ('London', 9558.561322414535), ('Tokyo', 0.00012771038834187613)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE numbers(x INTEGER)')
conn.executemany('INSERT INTO numbers VALUES (?)', [(i,) for i in range(10)])

rel = conn.sql('SELECT x FROM numbers WHERE x > 5')
print(rel.execute().fetchall())