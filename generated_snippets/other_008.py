# Generated: 2025-03-16 22:50:13.391651
# Result: (4, 'David', 3)
# Valid: True
import duckdb

con = duckdb.connect(':memory:')
con.execute('CREATE TABLE departments (id INT, dept_name VARCHAR)')
con.execute("INSERT INTO departments VALUES (1, 'Sales'), (2, 'Marketing'), (3, 'Engineering')")