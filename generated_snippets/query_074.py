# Generated: 2025-03-16 22:50:29.284671
# Result: ('Engineering',)
# Valid: True
import duckdb

con = duckdb.connect(':memory:')
con.execute('CREATE TABLE departments (id INT, dept_name VARCHAR)')
con.execute("INSERT INTO departments VALUES (1, 'Sales'), (2, 'Marketing'), (3, 'Engineering')")

result = con.execute('SELECT dept_name FROM departments WHERE id = 3').fetchone()
print(result)