# Generated: 2025-03-19 16:39:09.532993
# Result: [(1, 'John', None, 0), (2, 'Alice', 1, 1), (3, 'Bob', 1, 1), (4, 'Charlie', 2, 2), (5, 'David', 3, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create organizational hierarchy table
conn.execute('''
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    manager_id INTEGER
);
''')

# Insert hierarchical data
conn.executemany('INSERT INTO employees VALUES (?, ?, ?)', [
    (1, 'John', None),   # CEO
    (2, 'Alice', 1),     # Reports to John
    (3, 'Bob', 1),       # Reports to John
    (4, 'Charlie', 2),   # Reports to Alice
    (5, 'David', 3)      # Reports to Bob
])

# Recursive CTE to find full reporting chain
result = conn.execute('''
WITH RECURSIVE reporting_chain AS (
    SELECT employee_id, name, manager_id, 0 as depth
    FROM employees WHERE manager_id IS NULL

    UNION ALL

    SELECT e.employee_id, e.name, e.manager_id, rc.depth + 1
    FROM employees e
    JOIN reporting_chain rc ON e.manager_id = rc.employee_id
)
SELECT * FROM reporting_chain
''').fetchall()

print(result)