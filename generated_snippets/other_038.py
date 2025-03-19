# Generated: 2025-03-19 14:37:12.852952
# Result: [(datetime.datetime(2023, 6, 1, 0, 0), 22.5, 22.5), (datetime.datetime(2023, 6, 1, 1, 0), 21.299999237060547, 21.899999618530273), (datetime.datetime(2023, 6, 1, 2, 0), 20.100000381469727, 20.699999809265137), (datetime.datetime(2023, 6, 1, 3, 0), 19.700000762939453, 19.90000057220459)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a simple table and perform a basic query
conn.execute('CREATE TABLE numbers (id INTEGER, value INTEGER)')
conn.execute('INSERT INTO numbers VALUES (1, 10), (2, 20), (3, 30)')

rel = conn.table('numbers').filter('value > 15')
print(rel.execute().fetchall())