# Generated: 2025-03-19 08:06:42.790654
# Result: [('Engineering', 6000.0, 1)]
# Valid: True
import duckdb

# Create an in-memory database
conn = duckdb.connect(':memory:')

# Create tables for employees and departments
conn.execute('''
CREATE TABLE employees (
    id INT,
    name VARCHAR,
    department_id INT,
    salary DECIMAL(10,2)
);

CREATE TABLE departments (
    id INT,
    name VARCHAR
);

INSERT INTO employees VALUES
    (1, 'Alice', 1, 5000.00),
    (2, 'Bob', 2, 6000.00),
    (3, 'Charlie', 1, 5500.00);

INSERT INTO departments VALUES
    (1, 'Sales'),
    (2, 'Engineering');
''');

# Perform a complex join with aggregation and subquery
result = conn.execute('''
SELECT 
    d.name AS department, 
    AVG(e.salary) AS avg_salary,
    COUNT(*) AS employee_count
FROM employees e
JOIN departments d ON e.department_id = d.id
GROUP BY d.name
HAVING AVG(e.salary) > (
    SELECT AVG(salary) FROM employees
)
''').fetchall()

for row in result:
    print(row)