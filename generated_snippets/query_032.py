# Generated: 2025-03-16 22:39:44.169313
# Result: [(3, 'Charlie', 'Sales', Decimal('55000.00'), 1), (1, 'Alice', 'Sales', Decimal('50000.00'), 2), (4, 'David', 'Engineering', Decimal('80000.00'), 1), (2, 'Bob', 'Engineering', Decimal('75000.00'), 2)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample table and insert data
conn.execute('CREATE TABLE employees (id INT, name VARCHAR, department VARCHAR, salary DECIMAL(10,2))')
conn.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', [
    (1, 'Alice', 'Sales', 50000.00),
    (2, 'Bob', 'Engineering', 75000.00),
    (3, 'Charlie', 'Sales', 55000.00),
    (4, 'David', 'Engineering', 80000.00)
])

# Perform a window function query to rank employees by salary within each department
result = conn.execute('''
    SELECT 
        id, 
        name, 
        department, 
        salary,
        RANK() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank
    FROM employees
''').fetchall()

for row in result:
    print(row)