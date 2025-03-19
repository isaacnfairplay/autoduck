# Generated: 2025-03-19 16:27:44.629756
# Result: [('Marketing', 57500.0, 2)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample table of employees
conn.execute('''
CREATE TABLE employees (
    id INTEGER,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2)
);

INSERT INTO employees VALUES
    (1, 'Alice', 'Sales', 50000),
    (2, 'Bob', 'Marketing', 55000),
    (3, 'Charlie', 'Sales', 52000),
    (4, 'David', 'Marketing', 60000);
'''
)

# Demonstrate group-level aggregation with filtering
result = conn.execute('''
SELECT 
    department, 
    AVG(salary) as avg_salary,
    COUNT(*) as employee_count
FROM employees
GROUP BY department
HAVING AVG(salary) > 52000
''').fetchall()

for row in result:
    print(row)