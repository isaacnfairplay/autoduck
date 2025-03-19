# Generated: 2025-03-19 13:22:01.565961
# Result: [('Engineering', 80000.0, 'David'), ('Sales', 80000.0, 'Bob'), ('Marketing', 55000.0, 'Eve')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Nested subquery with lateral join demonstrating correlated aggregation
conn.execute('''CREATE TABLE departments (dept_id INT, dept_name TEXT)''')
conn.execute('''CREATE TABLE employees (emp_id INT, name TEXT, salary DECIMAL(10,2), dept_id INT)''')

conn.execute('''INSERT INTO departments VALUES (1, 'Sales'), (2, 'Engineering'), (3, 'Marketing')''')
conn.execute('''INSERT INTO employees VALUES 
    (101, 'Alice', 75000, 1), 
    (102, 'Bob', 85000, 1), 
    (103, 'Charlie', 95000, 2), 
    (104, 'David', 65000, 2), 
    (105, 'Eve', 55000, 3)''')

result = conn.execute('''
SELECT 
    d.dept_name, 
    avg_salary, 
    top_earner_name
FROM departments d
CROSS JOIN LATERAL (
    SELECT 
        AVG(salary) as avg_salary,
        MAX(name) as top_earner_name
    FROM employees e
    WHERE e.dept_id = d.dept_id
) dept_stats
''').fetchall()

for row in result:
    print(f"Department: {row[0]}, Avg Salary: ${row[1]:.2f}, Top Earner: {row[2]}")