# Generated: 2025-03-19 09:35:43.025361
# Result: [('Engineering', 'Bob', Decimal('160000.00'), 80000.0), ('Sales', 'Charlie', Decimal('65000.00'), 65000.0), ('Marketing', 'David', Decimal('70000.00'), 70000.0), ('Engineering', 'Alice', Decimal('160000.00'), 80000.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create employee and department tables
conn.sql('''
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name VARCHAR
);

CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name VARCHAR,
    dept_id INTEGER,
    salary DECIMAL(10,2)
);

INSERT INTO departments VALUES
    (1, 'Engineering'),
    (2, 'Sales'),
    (3, 'Marketing');

INSERT INTO employees VALUES
    (101, 'Alice', 1, 75000),
    (102, 'Bob', 1, 85000),
    (103, 'Charlie', 2, 65000),
    (104, 'David', 3, 70000);
''');

# Use lateral join to compute department-level salary statistics
result = conn.sql('''
SELECT 
    d.dept_name,
    e.name,
    total_dept_salary,
    avg_dept_salary
FROM departments d
LEFT JOIN LATERAL (
    SELECT 
        name,
        SUM(salary) OVER (PARTITION BY dept_id) as total_dept_salary,
        AVG(salary) OVER (PARTITION BY dept_id) as avg_dept_salary
    FROM employees
    WHERE dept_id = d.dept_id
) e ON TRUE
''').fetchall()

print(result)