# Generated: 2025-03-19 14:34:41.127877
# Result: [('CEO', 1), ('CEO -> CTO', 2), ('CEO -> CFO', 2), ('CEO -> CTO -> Senior Engineer', 3), ('CEO -> CTO -> Senior Engineer -> Junior Engineer', 4)]
# Valid: True
# Variable path: Type: str
# Attributes/Methods: capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix, removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
# Variable depth: Type: int
# Attributes/Methods: as_integer_ratio, bit_count, bit_length, conjugate, denominator, from_bytes, imag, is_integer, numerator, real, to_bytes
import duckdb

conn = duckdb.connect(':memory:')

# Create hierarchical organization data
conn.execute('''CREATE TABLE org_hierarchy (
    employee_id INTEGER,
    name VARCHAR,
    manager_id INTEGER
)''')

conn.execute('''INSERT INTO org_hierarchy VALUES
    (1, 'CEO', NULL),
    (2, 'CTO', 1),
    (3, 'CFO', 1),
    (4, 'Senior Engineer', 2),
    (5, 'Junior Engineer', 4)''')

# Use recursive CTE to show reporting structure
result = conn.execute('''
WITH RECURSIVE reporting_chain AS (
    SELECT employee_id, name, manager_id, name AS full_path, 1 AS depth
    FROM org_hierarchy WHERE manager_id IS NULL
    UNION ALL
    SELECT 
        o.employee_id, 
        o.name, 
        o.manager_id, 
        rc.full_path || ' -> ' || o.name,
        rc.depth + 1
    FROM org_hierarchy o
    JOIN reporting_chain rc ON o.manager_id = rc.employee_id
)
SELECT full_path, depth FROM reporting_chain
ORDER BY depth
''').fetchall()

for path, depth in result:
    print(f"Path: {path}, Depth: {depth}")