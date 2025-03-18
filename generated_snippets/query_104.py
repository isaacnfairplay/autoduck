# Generated: 2025-03-17 19:56:43.270046
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
# Variable result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
# Variable query: Type: str
# Attributes/Methods: capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix, removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
# Variable row: Type: tuple
# Attributes/Methods: count, index
import duckdb

# Create an in-memory DuckDB connection
conn = duckdb.connect(':memory:')

# Create sample tables
conn.execute('CREATE TABLE employees (id INT, name VARCHAR, department VARCHAR, salary DECIMAL)')
conn.execute('CREATE TABLE departments (dept_id VARCHAR, budget DECIMAL)')

# Insert sample data
conn.execute("""INSERT INTO employees VALUES
    (1, 'Alice', 'Sales', 50000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Sales', 55000),
    (4, 'David', 'Engineering', 75000)
""")

conn.execute("""INSERT INTO departments VALUES
    ('Sales', 250000),
    ('Marketing', 200000),
    ('Engineering', 500000)
""")

# Advanced query demonstrating complex join and window function
query = '''
    SELECT 
        e.name, 
        e.department, 
        e.salary,
        AVG(e.salary) OVER (PARTITION BY e.department) as dept_avg_salary,
        d.budget,
        DENSE_RANK() OVER (ORDER BY e.salary DESC) as salary_rank
    FROM employees e
    JOIN departments d ON e.department = d.dept_id
    ORDER BY salary_rank
'''

result = conn.execute(query).fetchall()
for row in result:
    print(row)

# Close the connection
conn.close()