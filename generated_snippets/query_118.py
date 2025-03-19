# Generated: 2025-03-19 12:58:06.306747
# Result: [(1, 'Alice', None, 'Alice'), (2, 'Bob', 1, 'Alice -> Bob'), (3, 'Charlie', 1, 'Alice -> Charlie'), (4, 'David', 2, 'Alice -> Bob -> David'), (5, 'Eve', 3, 'Alice -> Charlie -> Eve')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create employee hierarchy table
conn.execute('''
CREATE TABLE employees (
    id INT,
    name VARCHAR,
    manager_id INT
);

INSERT INTO employees VALUES
    (1, 'Alice', NULL),
    (2, 'Bob', 1),
    (3, 'Charlie', 1),
    (4, 'David', 2),
    (5, 'Eve', 3)
''')

# Recursive CTE to find reporting hierarchy
result = conn.execute('''
WITH RECURSIVE reporting_chain AS (
    SELECT id, name, manager_id, name AS path
    FROM employees WHERE manager_id IS NULL
    
    UNION ALL
    
    SELECT e.id, e.name, e.manager_id, rc.path || ' -> ' || e.name
    FROM employees e
    JOIN reporting_chain rc ON e.manager_id = rc.id
)
SELECT * FROM reporting_chain
''').fetchall()

for row in result:
    print(row)