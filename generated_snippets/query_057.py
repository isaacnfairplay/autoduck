# Generated: 2025-03-16 22:45:38.121628
# Result: [('North', 'B', Decimal('1500.000'), Decimal('2500.000'), 1), ('East', 'A', Decimal('1300.000'), Decimal('2400.000'), 2), ('South', 'B', Decimal('1200.000'), Decimal('2000.000'), 3), ('East', 'B', Decimal('1100.000'), Decimal('2400.000'), 4), ('North', 'A', Decimal('1000.000'), Decimal('2500.000'), 5), ('South', 'A', Decimal('800.000'), Decimal('2000.000'), 6)]
# Valid: True
# Variable results: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
# Variable recursive_query: Type: str
# Attributes/Methods: capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix, removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
import duckdb

# Advanced Recursive Common Table Expression (CTE) Example
con = duckdb.connect(':memory:')

# Create a hierarchical organization structure
con.execute('''
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR,
    manager_id INT
);

INSERT INTO employees VALUES 
    (1, 'CEO', NULL),
    (2, 'CTO', 1),
    (3, 'CFO', 1),
    (4, 'Engineering Manager', 2),
    (5, 'Finance Manager', 3)
''')

# Recursive CTE to show organizational hierarchy
recursive_query = '''
WITH RECURSIVE org_hierarchy(emp_id, name, manager_id, level) AS (
    SELECT emp_id, name, manager_id, 0
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT e.emp_id, e.name, e.manager_id, oh.level + 1
    FROM employees e
    JOIN org_hierarchy oh ON e.manager_id = oh.emp_id
)
SELECT * FROM org_hierarchy
ORDER BY level, emp_id
'''

results = con.execute(recursive_query).fetchall()
for row in results:
    print(f'Level {row[3]}: {row[1]}')