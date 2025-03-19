# Generated: 2025-03-19 10:01:57.662481
# Result: [('Engineering', 'Alice', 75000), ('Engineering', 'Bob', 65000), ('Sales', 'Charlie', 80000)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create tables for lateral join example
conn.execute('''
CREATE TABLE departments (dept_id INT, dept_name VARCHAR);
CREATE TABLE employees (emp_id INT, name VARCHAR, salary INT, dept_id INT);

INSERT INTO departments VALUES (1, 'Engineering'), (2, 'Sales');
INSERT INTO employees VALUES 
(101, 'Alice', 75000, 1),
(102, 'Bob', 65000, 1),
(103, 'Charlie', 80000, 2);
''');

# Perform lateral join to get top 2 earners per department
result = conn.execute('''
SELECT 
    d.dept_name, 
    e.name, 
    e.salary
FROM departments d,
    LATERAL (
        SELECT name, salary
        FROM employees
        WHERE dept_id = d.dept_id
        ORDER BY salary DESC
        LIMIT 2
    ) e
''').fetchall()

for row in result:
    print(row)