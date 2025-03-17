# Generated: 2025-03-16 22:53:03.861454
# Result: [(1, 'Alice', 'Sales'), (2, 'Bob', 'Marketing'), (3, 'Charlie', 'Sales')]
# Valid: True
import duckdb

con = duckdb.connect(':memory:')

con.execute('CREATE TABLE employees (id INT, name VARCHAR, department_id INT)')
con.execute('CREATE TABLE departments (id INT, dept_name VARCHAR)')

con.execute("INSERT INTO employees VALUES (1, 'Alice', 101), (2, 'Bob', 102), (3, 'Charlie', 101)")
con.execute("INSERT INTO departments VALUES (101, 'Sales'), (102, 'Marketing')")

result = con.execute('''
SELECT 
    e.id, 
    e.name, 
    d.dept_name
FROM employees e
JOIN departments d ON e.department_id = d.id
''').fetchall()

print(result)