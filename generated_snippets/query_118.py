# Generated: 2025-03-19 12:11:35.738385
# Result: [('Sales', 'Bob'), ('Engineering', 'David'), ('Marketing', 'Eve'), ('Sales', 'Alice'), ('Engineering', 'Charlie')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create departments and employees tables
conn.execute('CREATE TABLE departments(dept_id INTEGER, dept_name VARCHAR)')
conn.execute('CREATE TABLE employees(emp_id INTEGER, dept_id INTEGER, name VARCHAR)')

# Insert sample data
conn.executemany('INSERT INTO departments VALUES (?, ?)', [(1, 'Sales'), (2, 'Engineering'), (3, 'Marketing')])
conn.executemany('INSERT INTO employees VALUES (?, ?, ?)', [(1, 1, 'Alice'), (2, 1, 'Bob'), (3, 2, 'Charlie'), (4, 2, 'David'), (5, 3, 'Eve')])

# Use LATERAL join to get employees per department dynamically
result = conn.execute('''
SELECT 
    d.dept_name, 
    e.name as employee_name
FROM 
    departments d,
    LATERAL (SELECT name FROM employees WHERE dept_id = d.dept_id) e
''').fetchall()

print(result)