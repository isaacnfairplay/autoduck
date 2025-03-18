# Generated: 2025-03-16 23:54:08.467818
# Result: [(3, 'Sales', Decimal('60000.00'), 1), (1, 'Sales', Decimal('50000.00'), 2), (4, 'IT', Decimal('70000.00'), 1), (2, 'Marketing', Decimal('55000.00'), 1)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample table and insert data
conn.execute('''
    CREATE TABLE employees (
        employee_id INT,
        department VARCHAR,
        salary DECIMAL(10,2)
    );
    INSERT INTO employees VALUES
        (1, 'Sales', 50000.00),
        (2, 'Marketing', 55000.00),
        (3, 'Sales', 60000.00),
        (4, 'IT', 70000.00);
''')

# Perform a window function to rank employees by salary within each department
result = conn.execute('''
    SELECT 
        employee_id, 
        department, 
        salary,
        RANK() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank
    FROM employees
''').fetchall()

# Print results
for row in result:
    print(row)