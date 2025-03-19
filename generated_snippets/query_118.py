# Generated: 2025-03-19 16:52:08.995262
# Result: [(1, datetime.datetime(2023, 6, 1, 10, 0), 22.5, 22.5), (1, datetime.datetime(2023, 6, 1, 11, 0), 23.100000381469727, 22.800000190734863), (1, datetime.datetime(2023, 6, 1, 12, 0), 23.700000762939453, 23.40000057220459), (2, datetime.datetime(2023, 6, 1, 10, 0), 21.299999237060547, 21.299999237060547)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE numbers (value INT)')
conn.executemany('INSERT INTO numbers VALUES (?)', [(x,) for x in range(1, 6)])

rel = conn.sql('SELECT value, value * value as squared FROM numbers')
print(rel.execute().fetchall())