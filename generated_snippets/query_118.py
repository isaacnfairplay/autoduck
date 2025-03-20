# Generated: 2025-03-19 21:15:39.507512
# Result: [(1, 'Alice', 0, 'Alice'), (2, 'Bob', 1, 'Alice -> Bob'), (3, 'Charlie', 1, 'Alice -> Charlie'), (4, 'David', 2, 'Alice -> Bob -> David')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create hierarchical organizational data
conn.sql('''
CREATE TABLE org_hierarchy (
    employee_id INTEGER,
    name VARCHAR,
    manager_id INTEGER
);

INSERT INTO org_hierarchy VALUES
    (1, 'Alice', NULL),
    (2, 'Bob', 1),
    (3, 'Charlie', 1),
    (4, 'David', 2);
''');

# Recursive CTE to generate full reporting chain
result = conn.sql('''
WITH RECURSIVE reporting_chain(employee_id, name, level, path) AS (
    SELECT employee_id, name, 0, CAST(name AS VARCHAR) 
    FROM org_hierarchy 
    WHERE manager_id IS NULL
    UNION ALL
    SELECT 
        e.employee_id, 
        e.name, 
        rc.level + 1, 
        rc.path || ' -> ' || e.name
    FROM org_hierarchy e
    JOIN reporting_chain rc ON e.manager_id = rc.employee_id
)
SELECT * FROM reporting_chain
''').fetchall()

print(result)