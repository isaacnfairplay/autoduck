# Generated: 2025-03-19 13:13:28.240673
# Result: [(1, 'Alice', 'Alice'), (2, 'Bob', 'Alice -> Bob'), (3, 'Charlie', 'Alice -> Charlie'), (4, 'David', 'Alice -> Bob -> David'), (5, 'Eve', 'Alice -> Charlie -> Eve')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create graph-like hierarchy data
conn.execute('CREATE TABLE org_hierarchy (id INT, name TEXT, manager_id INT)')
conn.execute('''INSERT INTO org_hierarchy VALUES
    (1, 'Alice', NULL),
    (2, 'Bob', 1),
    (3, 'Charlie', 1),
    (4, 'David', 2),
    (5, 'Eve', 3)''')

# Use recursive CTE to traverse organizational hierarchy
result = conn.execute('''WITH RECURSIVE hierarchy_path(id, name, path) AS (
    SELECT id, name, CAST(name AS VARCHAR) FROM org_hierarchy WHERE manager_id IS NULL
    UNION ALL
    SELECT h.id, h.name, hp.path || ' -> ' || h.name
    FROM org_hierarchy h
    JOIN hierarchy_path hp ON h.manager_id = hp.id
)
SELECT * FROM hierarchy_path''').fetchall()

for row in result:
    print(row)