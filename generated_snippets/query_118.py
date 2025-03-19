# Generated: 2025-03-19 16:12:56.270661
# Result: [([4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate hierarchical data processing using recursive CTE
conn.execute('''
CREATE TABLE org_hierarchy (
    employee_id INT,
    name VARCHAR,
    manager_id INT
);

INSERT INTO org_hierarchy VALUES
    (1, 'CEO', NULL),
    (2, 'CTO', 1),
    (3, 'CFO', 1),
    (4, 'Senior Engineer', 2),
    (5, 'Junior Engineer', 4);

WITH RECURSIVE reporting_chain AS (
    SELECT employee_id, name, manager_id, name AS hierarchy_path
    FROM org_hierarchy WHERE manager_id IS NULL
    UNION ALL
    SELECT o.employee_id, o.name, o.manager_id, 
           rc.hierarchy_path || ' > ' || o.name
    FROM org_hierarchy o
    JOIN reporting_chain rc ON o.manager_id = rc.employee_id
)
SELECT * FROM reporting_chain
''').fetchall()