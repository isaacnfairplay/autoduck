# Generated: 2025-03-19 11:56:33.488578
# Result: [(1, 'Sales'), (2, 'Marketing'), (3, 'Engineering')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE departments(dept_id INTEGER, dept_name VARCHAR)')
conn.executemany('INSERT INTO departments VALUES (?, ?)', [
    (1, 'Sales'),
    (2, 'Marketing'),
    (3, 'Engineering')
])

result = conn.execute('SELECT * FROM departments').fetchall()
print(result)