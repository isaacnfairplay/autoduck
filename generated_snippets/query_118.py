# Generated: 2025-03-19 18:44:31.224788
# Result: [('Engineering', 'Diana', Decimal('75000.00'), 75000.0, 1), ('Marketing', 'Bob', Decimal('60000.00'), 60000.0, 2), ('Sales', 'Alice', Decimal('55000.00'), 53500.0, 3), ('Sales', 'Charlie', Decimal('52000.00'), 53500.0, 4)]
# Valid: True
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create a sample employees table
conn.execute('''
    CREATE TABLE employees (
        id INT, 
        name VARCHAR, 
        department VARCHAR, 
        salary DECIMAL(10,2)
    );
''')

# Insert sample data
conn.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', [
    (1, 'Alice', 'Sales', 55000.00),
    (2, 'Bob', 'Marketing', 60000.00),
    (3, 'Charlie', 'Sales', 52000.00),
    (4, 'Diana', 'Engineering', 75000.00)
])

# Complex query demonstrating window functions and aggregations
result = conn.execute('''
    SELECT 
        department, 
        name, 
        salary,
        AVG(salary) OVER (PARTITION BY department) as dept_avg_salary,
        RANK() OVER (ORDER BY salary DESC) as salary_rank
    FROM employees
''').fetchall()

print(result)