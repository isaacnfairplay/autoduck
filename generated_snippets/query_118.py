# Generated: 2025-03-19 11:53:58.330072
# Result: [(1, 'Sales', Decimal('55000.00'), 4.5, 0.0, 1), (3, 'Sales', Decimal('58000.00'), 4.699999809265137, 1.0, 2), (4, 'Marketing', Decimal('59000.00'), 3.9000000953674316, 0.0, 1), (2, 'Marketing', Decimal('62000.00'), 4.199999809265137, 1.0, 2)]
# Valid: True
import duckdb

# Create an in-memory database
conn = duckdb.connect(':memory:')

# Create a table with employee performance data
conn.execute('CREATE TABLE employees (id INT, department TEXT, salary DECIMAL(10,2), performance_score FLOAT)')
conn.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', [
    (1, 'Sales', 55000.00, 4.5),
    (2, 'Marketing', 62000.00, 4.2),
    (3, 'Sales', 58000.00, 4.7),
    (4, 'Marketing', 59000.00, 3.9)
])

# Use window functions to calculate percentile rank within departments
result = conn.execute('''
    SELECT 
        id, 
        department, 
        salary, 
        performance_score,
        PERCENT_RANK() OVER (PARTITION BY department ORDER BY performance_score) as perf_percentile,
        NTILE(4) OVER (PARTITION BY department ORDER BY salary) as salary_quartile
    FROM employees
''').fetchall()

print(result)