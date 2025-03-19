# Generated: 2025-03-19 19:24:45.429115
# Result: [(1, 'Alice', None, 'Alice'), (2, 'Bob', 1, 'Alice -> Bob'), (4, 'David', 2, 'Alice -> Bob -> David'), (3, 'Charlie', 1, 'Alice -> Charlie'), (5, 'Eve', 3, 'Alice -> Charlie -> Eve')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a graph-like adjacency table of employees and their managers
conn.execute('''CREATE TABLE employee_hierarchy (
    employee_id INTEGER,
    name VARCHAR,
    manager_id INTEGER
)''')

conn.execute('''INSERT INTO employee_hierarchy VALUES
    (1, 'Alice', NULL),
    (2, 'Bob', 1),
    (3, 'Charlie', 1),
    (4, 'David', 2),
    (5, 'Eve', 3)''')

# Use recursive common table expression to trace reporting paths
result = conn.execute('''WITH RECURSIVE reporting_chain AS (
    SELECT employee_id, name, manager_id, name as path
    FROM employee_hierarchy WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.name, e.manager_id, 
           rc.path || ' -> ' || e.name
    FROM employee_hierarchy e
    JOIN reporting_chain rc ON e.manager_id = rc.employee_id
)
SELECT * FROM reporting_chain ORDER BY path''').fetchall()

for row in result:
    print(f'Employee Path: {row[2]}')