# Generated: 2025-03-19 19:33:25.955709
# Result: [('Alice', 'Sales', Decimal('55000.00'), 1), ('Charlie', 'Sales', Decimal('52000.00'), 2), ('David', 'Engineering', Decimal('75000.00'), 1), ('Bob', 'Marketing', Decimal('60000.00'), 1), ('Eve', 'Marketing', Decimal('58000.00'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample employee data with departments
conn.execute('''
CREATE TABLE employees (
    id INT,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2)
);

INSERT INTO employees VALUES
(1, 'Alice', 'Sales', 55000),
(2, 'Bob', 'Marketing', 60000),
(3, 'Charlie', 'Sales', 52000),
(4, 'David', 'Engineering', 75000),
(5, 'Eve', 'Marketing', 58000);
''')

# Use window function to calculate department salary rankings
result = conn.execute('''
SELECT 
    name, 
    department, 
    salary,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_salary_rank
FROM employees
''').fetchall()

print(result)