# Generated: 2025-03-19 20:01:03.695231
# Result: [(1, 'Alice', 0, 'Alice'), (2, 'Bob', 1, 'Alice -> Bob'), (3, 'Charlie', 1, 'Alice -> Charlie'), (4, 'David', 2, 'Alice -> Bob -> David'), (5, 'Eve', 2, 'Alice -> Charlie -> Eve')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create organizational hierarchy table
conn.execute('CREATE TABLE employees (id INT, name TEXT, manager_id INT)')
conn.executemany('INSERT INTO employees VALUES (?, ?, ?)', [
    [1, 'Alice', None],
    [2, 'Bob', 1],
    [3, 'Charlie', 1],
    [4, 'David', 2],
    [5, 'Eve', 3]
])

# Recursive CTE to trace full management chain
result = conn.execute('''
WITH RECURSIVE management_chain(id, name, level, path) AS (
    SELECT id, name, 0, CAST(name AS VARCHAR) 
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, mc.level + 1, mc.path || ' -> ' || e.name
    FROM employees e
    JOIN management_chain mc ON e.manager_id = mc.id
)
SELECT * FROM management_chain
''').fetchall()

for row in result:
    print(row)