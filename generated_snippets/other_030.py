# Generated: 2025-03-19 11:59:00.510953
# Result: [(1, 'Alice', 1), (2, 'Bob', 2), (3, 'Charlie', 1), (4, 'David', 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE departments(dept_id INTEGER, dept_name VARCHAR)')
conn.executemany('INSERT INTO departments VALUES (?, ?)', [(1, 'Sales'), (2, 'Engineering')])