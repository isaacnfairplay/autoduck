# Generated: 2025-03-19 13:37:22.262728
# Result: [('Marketing', None, None, None, None), ('Sales', 'Alice', Decimal('5000.00'), Decimal('5000.00'), Decimal('5000.00')), ('Engineering', 'Bob', Decimal('6500.50'), Decimal('6500.50'), Decimal('6500.50')), ('Engineering', 'Charlie', Decimal('7200.75'), Decimal('6500.50'), Decimal('7200.75'))]
# Valid: True
import duckdb

# Demonstrate lateral join with subquery generation
conn = duckdb.connect(':memory:')

# Create tables with related data
conn.execute('CREATE TABLE departments (dept_id INT, dept_name VARCHAR)')
conn.execute('CREATE TABLE employees (emp_id INT, name VARCHAR, dept_id INT, salary DECIMAL(10,2))')

conn.executemany('INSERT INTO departments VALUES (?, ?)', [
    (1, 'Sales'), (2, 'Engineering'), (3, 'Marketing')
])

conn.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', [
    (101, 'Alice', 1, 5000.00),
    (102, 'Bob', 2, 6500.50),
    (103, 'Charlie', 2, 7200.75)
])

# Use lateral join to generate employee salary ranges per department
result = conn.execute('''
    SELECT 
        d.dept_name, 
        e.name, 
        e.salary,
        FIRST_VALUE(e.salary) OVER (PARTITION BY d.dept_id ORDER BY e.salary) as min_salary,
        LAST_VALUE(e.salary) OVER (PARTITION BY d.dept_id ORDER BY e.salary) as max_salary
    FROM departments d
    LEFT JOIN LATERAL (
        SELECT * FROM employees WHERE dept_id = d.dept_id
    ) e ON TRUE
''').fetchall()

print(result)