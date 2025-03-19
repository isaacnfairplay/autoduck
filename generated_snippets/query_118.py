# Generated: 2025-03-19 12:16:55.853450
# Result: [('Sales', 'Bob', Decimal('60000.00'), 1), ('Engineering', 'David', Decimal('80000.00'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample employees table
conn.execute('''
CREATE TABLE employees (
    department VARCHAR,
    name VARCHAR,
    salary DECIMAL(10,2)
);

INSERT INTO employees VALUES
    ('Sales', 'Alice', 55000),
    ('Sales', 'Bob', 60000),
    ('Engineering', 'Charlie', 75000),
    ('Engineering', 'David', 80000),
    ('HR', 'Eve', 50000);
''')

# Correlated subquery with window function ranking
result = conn.execute('''
SELECT
    department,
    name,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_salary_rank
FROM employees e1
WHERE salary > (
    SELECT AVG(salary) 
    FROM employees e2 
    WHERE e2.department = e1.department
)
''').fetchall()

for row in result:
    print(row)