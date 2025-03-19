# Generated: 2025-03-19 12:02:12.674161
# Result: [('Sales',), ('Engineering',)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('CREATE TABLE departments(dept_id INTEGER, dept_name VARCHAR)')
conn.executemany('INSERT INTO departments VALUES (?, ?)', [(1, 'Sales'), (2, 'Engineering')])

result = conn.execute('SELECT dept_name FROM departments WHERE dept_id > 0').fetchall()
print(result)