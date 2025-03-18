# Generated: 2025-03-17 19:58:12.282933
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample employees table
conn.execute('''
CREATE TABLE employees (
    id INT,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2)
)''')

# Insert sample data
conn.execute('''
INSERT INTO employees VALUES
    (1, 'Alice', 'Sales', 50000.00),
    (2, 'Bob', 'Marketing', 60000.00),
    (3, 'Charlie', 'Engineering', 75000.00)
''')

# Complex query with window functions and aggregations
query = '''
SELECT 
    department,
    AVG(salary) as avg_salary,
    MAX(salary) as max_salary,
    RANK() OVER (ORDER BY AVG(salary) DESC) as dept_salary_rank
FROM employees
GROUP BY department
'''

results = conn.execute(query).fetchall()
for row in results:
    print(row)

conn.close()