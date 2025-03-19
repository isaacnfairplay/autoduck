# Generated: 2025-03-19 17:28:20.391787
# Result: [('Marketing', 'David', Decimal('65000.00'), 'David', 1), ('Marketing', 'Bob', Decimal('60000.00'), 'David', 2), ('Sales', 'Charlie', Decimal('55000.00'), 'Charlie', 3), ('Sales', 'Alice', Decimal('50000.00'), 'Charlie', 4)]
# Valid: True
import duckdb

con = duckdb.connect(':memory:')

# Create a nested subquery with lateral join and window functions
con.execute('''
CREATE TABLE employees (
    id INT,
    name TEXT,
    department TEXT,
    salary DECIMAL(10,2)
);

INSERT INTO employees VALUES
    (1, 'Alice', 'Sales', 50000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Sales', 55000),
    (4, 'David', 'Marketing', 65000);

SELECT 
    department, 
    name, 
    salary,
    FIRST_VALUE(name) OVER (PARTITION BY department ORDER BY salary DESC) as top_earner,
    DENSE_RANK() OVER (ORDER BY salary DESC) as salary_rank
FROM employees
''')

result = con.fetchall()
for row in result:
    print(row)