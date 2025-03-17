# Generated: 2025-03-16 22:50:00.254149
# Result: (3, 'Charlie', 'Sales')
# Valid: True
import duckdb

con = duckdb.connect(':memory:')
con.execute('CREATE TABLE departments (id INT, dept_name VARCHAR)')
con.execute('CREATE TABLE employees (id INT, name VARCHAR, department_id INT)')

con.execute("INSERT INTO departments VALUES (1, 'Sales'), (2, 'Marketing')")
con.execute("INSERT INTO employees VALUES (1, 'Alice', 1), (2, 'Bob', 2), (3, 'Charlie', 1)")

result = con.execute('''
SELECT 
    e.id, 
    e.name, 
    d.dept_name
FROM employees e
JOIN departments d ON e.department_id = d.id
WHERE e.id = 3
''').fetchone()

print(result)