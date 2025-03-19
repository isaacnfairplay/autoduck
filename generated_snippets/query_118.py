# Generated: 2025-03-19 18:13:41.286092
# Result: [('Marketing', 'David', Decimal('65000.00')), ('Marketing', 'Bob', Decimal('60000.00')), ('Sales', 'Alice', Decimal('55000.00')), ('Sales', 'Charlie', Decimal('52000.00'))]
# Valid: True
import duckdb

# Connect to an in-memory database
conn = duckdb.connect(':memory:')

# Create a table with employee data
conn.execute('''
    CREATE TABLE employees (
        id INTEGER,
        name VARCHAR,
        department VARCHAR,
        salary DECIMAL(10,2)
    );

    INSERT INTO employees VALUES
        (1, 'Alice', 'Sales', 55000.00),
        (2, 'Bob', 'Marketing', 60000.00),
        (3, 'Charlie', 'Sales', 52000.00),
        (4, 'David', 'Marketing', 65000.00);
''')

# Perform lateral join to get top 2 salaries per department
result = conn.execute('''
    SELECT 
        e.department, 
        e.name, 
        e.salary
    FROM employees e,
    LATERAL (
        SELECT name, salary
        FROM employees
        WHERE department = e.department
        ORDER BY salary DESC
        LIMIT 2
    ) top_salaries
    GROUP BY e.department, e.name, e.salary
    ORDER BY e.department, e.salary DESC
''').fetchall()

for row in result:
    print(row)