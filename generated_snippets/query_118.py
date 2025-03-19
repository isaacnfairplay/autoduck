# Generated: 2025-03-19 11:57:23.397685
# Result: [(1, 'Alice', 1), (2, 'Bob', 2), (3, 'Charlie', 1), (4, 'David', 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE employees(emp_id INTEGER, name VARCHAR, dept_id INTEGER)')
conn.executemany('INSERT INTO employees VALUES (?, ?, ?)', [
    (1, 'Alice', 1),
    (2, 'Bob', 2),
    (3, 'Charlie', 1),
    (4, 'David', 3)
])

result = conn.execute('SELECT * FROM employees').fetchall()
print(result)