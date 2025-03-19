# Generated: 2025-03-19 15:10:51.809395
# Result: [('Alice', 'Sales'), ('Bob', 'Engineering'), ('Charlie', 'Sales'), ('David', 'Marketing')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create tables for employees and departments
conn.execute('CREATE TABLE employees (emp_id INT, name TEXT, dept_id INT)')
conn.execute('CREATE TABLE departments (dept_id INT, dept_name TEXT)')

conn.executemany('INSERT INTO employees VALUES (?, ?, ?)', [
    (1, 'Alice', 1), (2, 'Bob', 2), (3, 'Charlie', 1), (4, 'David', 3)
])
conn.executemany('INSERT INTO departments VALUES (?, ?)', [
    (1, 'Sales'), (2, 'Engineering'), (3, 'Marketing')
])

# Perform lateral join to get employees with their department details
result = conn.execute('''
    SELECT e.name, d.dept_name
    FROM employees e,
    LATERAL (SELECT dept_name FROM departments WHERE dept_id = e.dept_id) d
''').fetchall()

for row in result:
    print(f'Employee: {row[0]}, Department: {row[1]}')