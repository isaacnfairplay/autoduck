# Generated: 2025-03-16 22:47:18.238740
# Result: [('Junior Engineer', 0), ('Senior Engineer', 1), ('CTO', 2), ('CEO', 3)]
# Valid: True
# Variable result_sql: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
# Variable level: Type: int
# Attributes/Methods: as_integer_ratio, bit_count, bit_length, conjugate, denominator, from_bytes, imag, is_integer, numerator, real, to_bytes
# Variable sql_approach: Type: function
# Variable relational_api_approach: Type: function
# Variable employee: Type: str
# Attributes/Methods: capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix, removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
# Variable start_rel: Type: float
# Attributes/Methods: as_integer_ratio, conjugate, fromhex, hex, imag, is_integer, real
# Variable start_sql: Type: float
# Attributes/Methods: as_integer_ratio, conjugate, fromhex, hex, imag, is_integer, real
import duckdb

con = duckdb.connect(':memory:')

# Create an employee hierarchy table
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
    (4, 'Senior Engineer', 2),
    (5, 'Junior Engineer', 4);
''')

# Recursive query to find entire management chain
result = con.execute('''
    WITH RECURSIVE management_chain AS (
        SELECT emp_id, name, manager_id, 0 as depth
        FROM employees
        WHERE emp_id = 5

        UNION ALL

        SELECT e.emp_id, e.name, e.manager_id, mc.depth + 1
        FROM employees e
        JOIN management_chain mc ON e.emp_id = mc.manager_id
    )
    SELECT name, depth FROM management_chain
    ORDER BY depth
''').fetchall()

for employee, level in result:
    print(f'Level {level}: {employee}')