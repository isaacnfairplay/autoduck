# Generated: 2025-03-19 09:29:27.337005
# Result: [('Sales', Decimal('45000.00'), Decimal('45000.00')), ('Sales', Decimal('50000.00'), Decimal('95000.00')), ('Engineering', Decimal('75000.00'), Decimal('75000.00')), ('Engineering', Decimal('80000.00'), Decimal('155000.00')), ('Marketing', Decimal('60000.00'), Decimal('60000.00'))]
# Valid: True
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create a table with employee salary data
conn.execute('''
CREATE TABLE employees (
    dept VARCHAR,
    salary DECIMAL(10,2)
);

INSERT INTO employees VALUES
('Sales', 50000.00),
('Marketing', 60000.00),
('Engineering', 75000.00),
('Sales', 45000.00),
('Engineering', 80000.00);
'''
)

# Calculate running total salary per department using window function
result = conn.execute('''
SELECT 
    dept, 
    salary,
    SUM(salary) OVER (PARTITION BY dept ORDER BY salary) as cumulative_dept_salary
FROM employees
''').fetchall()

print(result)