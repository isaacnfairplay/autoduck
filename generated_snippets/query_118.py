# Generated: 2025-03-19 21:11:21.940082
# Result: [('Sales', 'Alice', Decimal('55000.00'), 1, 53500.0), ('Sales', 'Charlie', Decimal('52000.00'), 2, 53500.0), ('Marketing', 'David', Decimal('65000.00'), 1, 62500.0), ('Marketing', 'Bob', Decimal('60000.00'), 2, 62500.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with employee data
conn.sql('''
CREATE TABLE employees (
    id INTEGER,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2)
);

INSERT INTO employees VALUES
    (1, 'Alice', 'Sales', 55000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Sales', 52000),
    (4, 'David', 'Marketing', 65000);
''');

# Perform complex group-level window function
result = conn.sql('''
SELECT
    department,
    name,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_salary_rank,
    AVG(salary) OVER (PARTITION BY department) as dept_avg_salary
FROM employees
''').fetchall()

print(result)