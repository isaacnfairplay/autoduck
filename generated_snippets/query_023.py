# Generated: 2025-03-16 22:16:38.976811
# Result: [('Bob', 'Engineering', Decimal('85000.00'), 85000.0, 1), ('Alice', 'Sales', Decimal('75000.00'), 73500.0, 2), ('David', 'Sales', Decimal('72000.00'), 73500.0, 3), ('Charlie', 'Marketing', Decimal('65000.00'), 65000.0, 4)]
# Valid: True
import duckdb

# Establish an in-memory database connection
con = duckdb.connect(':memory:')

# Create sample tables for advanced analytics
con.sql('''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2)
);

CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name VARCHAR,
    location VARCHAR
);
''')

# Insert sample data
con.sql('''
INSERT INTO departments VALUES
    (1, 'Sales', 'New York'),
    (2, 'Engineering', 'San Francisco'),
    (3, 'Marketing', 'Chicago');

INSERT INTO employees VALUES
    (1, 'Alice', 'Sales', 75000),
    (2, 'Bob', 'Engineering', 85000),
    (3, 'Charlie', 'Marketing', 65000),
    (4, 'David', 'Sales', 72000);
''')

# Advanced analytical query with window functions and joins
result = con.sql('''
SELECT 
    e.name,
    d.dept_name,
    e.salary,
    AVG(e.salary) OVER (PARTITION BY d.dept_name) AS avg_dept_salary,
    DENSE_RANK() OVER (ORDER BY e.salary DESC) AS salary_rank
FROM employees e
JOIN departments d ON e.department = d.dept_name
''').fetchall()

for row in result:
    print(row)