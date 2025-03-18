# Generated: 2025-03-16 22:53:17.617796
# Result: [('Alice', 'Sales'), ('Bob', 'Marketing'), ('Charlie', 'Sales')]
# Valid: True
import duckdb

con = duckdb.connect(':memory:')
con.execute('CREATE TABLE employees (id INT, name VARCHAR, department VARCHAR)')
con.execute("INSERT INTO employees VALUES (1, 'Alice', 'Sales'), (2, 'Bob', 'Marketing'), (3, 'Charlie', 'Sales')")

result = con.execute('SELECT name, department FROM employees').fetchall()
print(result)