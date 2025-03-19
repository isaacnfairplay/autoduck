# Generated: 2025-03-19 13:03:11.924660
# Result: [('Alice', 'Sales', 100000, 85, 0.0), ('Charlie', 'Sales', 95000, 90, 1.0), ('David', 'Engineering', 120000, 95, 0.0), ('Bob', 'Marketing', 90000, 75, 0.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('CREATE TABLE sample_data (id INT, value VARCHAR)')
conn.execute("INSERT INTO sample_data VALUES (1, 'hello'), (2, 'world')")

rel = conn.table('sample_data').filter('id = 1')
print(rel.execute().fetchall())