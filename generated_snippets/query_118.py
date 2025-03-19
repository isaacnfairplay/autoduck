# Generated: 2025-03-19 10:48:31.139191
# Result: [('Engineering', 88500.0, Decimal('92000.00'), 2), ('Sales', 72000.0, Decimal('72000.00'), 1), ('Marketing', 65000.0, Decimal('65000.00'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate employees table
conn.execute('''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary DECIMAL(10,2)
);
''')

conn.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', [
    (1, 'Alice', 'Engineering', 85000),
    (2, 'Bob', 'Sales', 72000),
    (3, 'Charlie', 'Engineering', 92000),
    (4, 'Diana', 'Marketing', 65000)
])

# Calculate department-level salary statistics
result = conn.execute('''
SELECT 
    department, 
    AVG(salary) as avg_salary,
    MAX(salary) as max_salary,
    COUNT(*) as employee_count
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
''').fetchall()

for row in result:
    print(f'Department: {row[0]}, Avg Salary: ${row[1]}, Max Salary: ${row[2]}, Employees: {row[3]}')