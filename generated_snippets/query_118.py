# Generated: 2025-03-19 12:45:57.520601
# Result: [('Alice', 'Sales', 50000, 1), ('Charlie', 'Sales', 55000, 2), ('David', 'Engineering', 75000, 1), ('Bob', 'Marketing', 60000, 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample employee data
conn.execute('''
CREATE TABLE employees AS
SELECT * FROM (VALUES
    (1, 'Alice', 'Sales', 50000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Sales', 55000),
    (4, 'David', 'Engineering', 75000)
) AS t(id, name, department, salary);
''')

# Use window function to calculate department-wise percentile rank of salaries
result = conn.execute('''SELECT 
    name, 
    department, 
    salary,
    NTILE(4) OVER (PARTITION BY department ORDER BY salary) as salary_quartile
FROM employees
''').fetchall()

for row in result:
    print(row)