# Generated: 2025-03-19 15:28:10.530679
# Result: [('CEO', 0), ('CFO', 1), ('CTO', 1), ('Senior Engineer', 2), ('Junior Engineer', 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create an employee hierarchy table
conn.execute('''
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        manager_id INTEGER
    );

    INSERT INTO employees VALUES
        (1, 'CEO', NULL),
        (2, 'CTO', 1),
        (3, 'CFO', 1),
        (4, 'Senior Engineer', 2),
        (5, 'Junior Engineer', 4)
''');

# Recursive query to generate organizational hierarchy
result = conn.execute('''
    WITH RECURSIVE org_hierarchy AS (
        SELECT id, name, manager_id, 0 as depth
        FROM employees
        WHERE manager_id IS NULL

        UNION ALL

        SELECT e.id, e.name, e.manager_id, oh.depth + 1
        FROM employees e
        JOIN org_hierarchy oh ON e.manager_id = oh.id
    )
    SELECT name, depth
    FROM org_hierarchy
    ORDER BY depth, name
''').fetchall()

for row in result:
    print(f'Employee: {row[0]}, Hierarchy Depth: {row[1]}')