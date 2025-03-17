# Generated: 2025-03-16 22:52:56.651014
# Result: [('Mid-range', 2, 799.99), ('Budget', 1, 299.99)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a table
con.execute('CREATE TABLE employees (id INT, name VARCHAR, department VARCHAR)')
con.execute("INSERT INTO employees VALUES (1, 'Alice', 'Sales'), (2, 'Bob', 'Marketing'), (3, 'Charlie', 'Sales')")

# Create a relation from the table
employees_rel = con.query('SELECT * FROM employees')

# Print relation details
print('Relation Columns:', employees_rel.columns)
print('Relation Types:', employees_rel.types)
print('Relation Data:', employees_rel.execute().fetchall())