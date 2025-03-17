# Generated: 2025-03-16 22:50:07.210388
# Result: (4, 'David', 3)
# Valid: True
import duckdb

con = duckdb.connect(':memory:')
con.execute('CREATE TABLE employees (id INT, name VARCHAR, department_id INT)')
con.execute('CREATE TABLE departments (id INT, dept_name VARCHAR)')

con.execute("INSERT INTO departments VALUES (1, 'Sales'), (2, 'Marketing'), (3, 'Engineering')")
con.execute("INSERT INTO employees VALUES (1, 'Alice', 1), (2, 'Bob', 2), (3, 'Charlie', 1), (4, 'David', 3)")

result = con.execute('''
SELECT 
    e.id, 
    e.name, 
    e.department_id
FROM employees e
WHERE e.id = 4
''').fetchone()

print(result)