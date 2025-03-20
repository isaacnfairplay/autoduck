# Generated: 2025-03-19 20:16:41.615981
# Result: [('Engineering', 'Bob', Decimal('85000.000')), ('Engineering', 'Charlie', Decimal('65000.000')), ('Marketing', 'David', Decimal('55000.000')), ('Sales', 'Alice', Decimal('75000.000'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create tables and perform lateral join to explore nested query capabilities
conn.execute("""CREATE TABLE departments (dept_id INT, dept_name VARCHAR)""")
conn.execute("""CREATE TABLE employees (emp_id INT, name VARCHAR, salary DECIMAL, dept_id INT)""")

conn.execute("""INSERT INTO departments VALUES (1, 'Sales'), (2, 'Engineering'), (3, 'Marketing')""")
conn.execute("""INSERT INTO employees VALUES 
    (101, 'Alice', 75000, 1), 
    (102, 'Bob', 85000, 2), 
    (103, 'Charlie', 65000, 2), 
    (104, 'David', 55000, 3)""")

# Perform lateral join to get top 2 earners per department
result = conn.execute("""
    SELECT d.dept_name, e.name, e.salary
    FROM departments d,
    LATERAL (
        SELECT name, salary 
        FROM employees e2 
        WHERE e2.dept_id = d.dept_id 
        ORDER BY salary DESC 
        LIMIT 2
    ) e
    ORDER BY d.dept_name, e.salary DESC
""").fetchall()

for row in result:
    print(f"Department: {row[0]}, Employee: {row[1]}, Salary: ${row[2]}")