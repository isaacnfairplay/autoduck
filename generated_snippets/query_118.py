# Generated: 2025-03-19 12:08:15.544898
# Result: [('Sales', 2), ('Engineering', 2), ('Marketing', 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create departments and employees tables
conn.execute('CREATE TABLE departments(dept_id INTEGER, dept_name VARCHAR)')
conn.execute('CREATE TABLE employees(emp_id INTEGER, dept_id INTEGER, name VARCHAR)')

# Insert sample data
conn.executemany('INSERT INTO departments VALUES (?, ?)', [(1, 'Sales'), (2, 'Engineering'), (3, 'Marketing')])
conn.executemany('INSERT INTO employees VALUES (?, ?, ?)', [(1, 1, 'Alice'), (2, 1, 'Bob'), (3, 2, 'Charlie'), (4, 2, 'David'), (5, 3, 'Eve')])

# Use correlated subquery to count employees per department
result = conn.execute('''SELECT dept_name, (SELECT COUNT(*) FROM employees sub WHERE sub.dept_id = d.dept_id) as dept_headcount FROM departments d''').fetchall()

print(result)