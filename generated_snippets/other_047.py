# Generated: 2025-03-19 17:55:37.098517
# Result: <duckdb.duckdb.DuckDBPyConnection object at 0x00000147DFA771F0>
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('CREATE TABLE numbers (value INTEGER)')
conn.executemany('INSERT INTO numbers VALUES (?)', [(x,) for x in range(1, 6)])

rel = conn.table('numbers').filter('value > 2').project('value * 2 AS doubled_value')
print(rel.execute().fetchall())