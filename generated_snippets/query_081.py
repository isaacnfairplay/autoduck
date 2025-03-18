# Generated: 2025-03-16 22:52:34.059083
# Result: [(1, 'Alice'), (2, 'Bob')]
# Valid: True
import duckdb

con = duckdb.connect(':memory:')
con.execute('CREATE TABLE employees (id INT, name VARCHAR, department VARCHAR)')
con.execute('CREATE TABLE departments (id INT, dept_name VARCHAR)')

con.execute("INSERT INTO employees VALUES (1, 'Alice', 'Sales'), (2, 'Bob', 'Marketing'), (3, 'Charlie', 'Sales')")
con.execute("INSERT INTO departments VALUES (1, 'Sales'), (2, 'Marketing'), (3, 'Engineering')")

employees_rel = con.query('SELECT * FROM employees')
departments_rel = con.query('SELECT * FROM departments')

join_result = employees_rel.join(departments_rel, 'department = dept_name')
print('Join Results:', join_result.execute().fetchall())