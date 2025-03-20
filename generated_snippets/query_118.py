# Generated: 2025-03-19 20:34:04.590283
# Result: [(1, 'Alice', None, 0), (4, 'David', None, 0), (2, 'Bob', 1, 1), (3, 'Charlie', 1, 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table for hierarchical organizational data
conn.execute('''
CREATE TABLE org_hierarchy (
    employee_id INTEGER,
    name VARCHAR,
    manager_id INTEGER,
    department VARCHAR,
    salary DECIMAL(10,2)
);''')

# Insert sample hierarchical employee data
conn.executemany('INSERT INTO org_hierarchy VALUES (?, ?, ?, ?, ?)', [
    (1, 'Alice', None, 'Engineering', 120000.00),
    (2, 'Bob', 1, 'Engineering', 95000.50),
    (3, 'Charlie', 1, 'Engineering', 85000.25),
    (4, 'David', None, 'Sales', 110000.75)
])

# Use recursive common table expression (CTE) to explore organizational hierarchy
result = conn.execute('''
WITH RECURSIVE org_tree(employee_id, name, manager_id, level) AS (
    SELECT employee_id, name, manager_id, 0
    FROM org_hierarchy
    WHERE manager_id IS NULL
    
    UNION ALL
    
    SELECT e.employee_id, e.name, e.manager_id, ot.level + 1
    FROM org_hierarchy e
    JOIN org_tree ot ON e.manager_id = ot.employee_id
)
SELECT * FROM org_tree
''').fetchall()

print(result)