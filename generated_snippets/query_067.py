# Generated: 2025-03-16 22:49:16.812754
# Result: [('Bob', 'Marketing', Decimal('60000.00'), 60000.0, 1), ('Charlie', 'Sales', Decimal('55000.00'), 52500.0, 2), ('Alice', 'Sales', Decimal('50000.00'), 52500.0, 3)]
# Valid: True
import duckdb

# Create an in-memory DuckDB connection
con = duckdb.connect(':memory:')

# Create sample tables for demonstrating complex queries
con.execute('''
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2)
);

CREATE TABLE departments (
    dept_id VARCHAR PRIMARY KEY,
    dept_name VARCHAR
);

INSERT INTO employees VALUES
    (1, 'Alice', 'Sales', 50000.00),
    (2, 'Bob', 'Marketing', 60000.00),
    (3, 'Charlie', 'Sales', 55000.00);

INSERT INTO departments VALUES
    ('Sales', 'Revenue Generation'),
    ('Marketing', 'Brand Strategy');
''')

# Demonstrate complex multi-table join with window function
result = con.execute('''
SELECT 
    e.name,
    e.department,
    e.salary,
    AVG(e.salary) OVER (PARTITION BY e.department) as dept_avg_salary,
    RANK() OVER (ORDER BY e.salary DESC) as salary_rank
FROM employees e
JOIN departments d ON e.department = d.dept_id
ORDER BY salary_rank
''').fetchall()

print(result)