# Generated: 2025-03-19 12:07:24.087455
# Result: []
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create organizations and employees tables
conn.execute('CREATE TABLE organizations(org_id INT, name TEXT)')
conn.execute('CREATE TABLE employees(emp_id INT, org_id INT, first_name TEXT, last_name TEXT, salary DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO organizations VALUES (?, ?)', [(1, 'TechCorp'), (2, 'DataInc')])
conn.executemany('INSERT INTO employees VALUES (?, ?, ?, ?, ?)', [
    (101, 1, 'Alice', 'Smith', 75000.00),
    (102, 1, 'Bob', 'Jones', 82000.00),
    (103, 2, 'Charlie', 'Brown', 68000.00)
])

# Complex join with aggregation and nested conditions
result = conn.execute('''
    SELECT 
        o.name as organization, 
        AVG(e.salary) as avg_salary,
        COUNT(*) as employee_count
    FROM organizations o
    JOIN employees e ON o.org_id = e.org_id
    WHERE e.salary > (
        SELECT AVG(salary) FROM employees
    )
    GROUP BY o.name
    HAVING COUNT(*) > 1
''').fetchall()

print(result)