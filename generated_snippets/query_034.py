# Generated: 2025-03-16 22:40:04.309129
# Result: [('Engineering', 75000.0, 1), ('Sales', 52500.0, 2)]
# Valid: True
import duckdb

# Establish an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample employees table
conn.execute('''
CREATE TABLE employees (
    id INT,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2)
)''')

# Insert sample employee data
conn.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', [
    (1, 'Alice', 'Sales', 50000.00),
    (2, 'Bob', 'Engineering', 75000.00),
    (3, 'Charlie', 'Sales', 55000.00)
])

# Perform an aggregation query with grouped results
result = conn.execute('''
SELECT 
    department, 
    AVG(salary) as avg_department_salary, 
    COUNT(*) as employee_count
FROM employees
GROUP BY department
''').fetchall()

for row in result:
    print(f'Department: {row[0]}, Average Salary: ${row[1]:.2f}, Employees: {row[2]}')