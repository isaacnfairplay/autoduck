# Generated: 2025-03-19 10:08:07.006150
# Result: [('Sales', 55000.0, 1), ('Marketing', 59000.0, 2)]
# Valid: True
import duckdb

# Connect to an in-memory database
conn = duckdb.connect(':memory:')

# Create a simple employees table
conn.execute('''
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        department VARCHAR,
        salary DECIMAL(10,2)
    );

    INSERT INTO employees VALUES
        (1, 'Alice', 'Sales', 55000),
        (2, 'Bob', 'Marketing', 60000),
        (3, 'Charlie', 'Sales', 52000),
        (4, 'David', 'Marketing', 58000)
''');

# Demonstrate group aggregation with filtering
result = conn.execute('''
    SELECT 
        department, 
        AVG(salary) as avg_salary,
        COUNT(*) as employee_count
    FROM employees
    WHERE salary > 53000
    GROUP BY department
''').fetchall()

for row in result:
    print(row)