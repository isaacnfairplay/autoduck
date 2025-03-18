# Generated: 2025-03-17 20:07:33.981726
# Result: [(4, 'David', 'Engineering', 1, 4.0), (2, 'Bob', 'Marketing', 1, 2.0), (1, 'Alice', 'Sales', 1, 2.0), (3, 'Charlie', 'Sales', 2, 2.0)]
# Valid: True
# Variable query: Type: str
# Attributes/Methods: capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix, removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
# Variable row: Type: tuple
# Attributes/Methods: count, index
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create sample tables
con.execute('''
    CREATE TABLE employees (
        employee_id INT, 
        name VARCHAR, 
        department_id INT
    );

    CREATE TABLE departments (
        department_id INT, 
        department_name VARCHAR
    );

    INSERT INTO employees VALUES 
        (1, 'Alice', 10), 
        (2, 'Bob', 20), 
        (3, 'Charlie', 10), 
        (4, 'David', 30);

    INSERT INTO departments VALUES 
        (10, 'Sales'), 
        (20, 'Marketing'), 
        (30, 'Engineering');
''')

# Complex multi-table join with window function
query = '''
    SELECT 
        e.employee_id, 
        e.name, 
        d.department_name,
        ROW_NUMBER() OVER (PARTITION BY d.department_name ORDER BY e.employee_id) as dept_rank,
        AVG(e.employee_id) OVER (PARTITION BY d.department_name) as avg_dept_employee_id
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
    ORDER BY d.department_name, dept_rank
'''

result = con.execute(query).fetchall()
for row in result:
    print(row)
