# Generated: 2025-03-19 16:49:37.024372
# Result: [(1, 'Alice', None, 0), (2, 'Bob', 1, 1), (3, 'Charlie', 1, 1), (4, 'David', 2, 2)]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create employee hierarchy table
conn.execute('''
    CREATE TABLE employees (
        id INT PRIMARY KEY,
        name VARCHAR,
        manager_id INT
    );
''')

# Insert hierarchical data
conn.executemany('INSERT INTO employees VALUES (?, ?, ?)', [
    (1, 'Alice', None),
    (2, 'Bob', 1),
    (3, 'Charlie', 1),
    (4, 'David', 2)
])

# Recursive CTE to show employee hierarchy
result = conn.execute('''
    WITH RECURSIVE employee_hierarchy AS (
        SELECT id, name, manager_id, 0 as depth
        FROM employees
        WHERE manager_id IS NULL
        UNION ALL
        SELECT e.id, e.name, e.manager_id, eh.depth + 1
        FROM employees e
        JOIN employee_hierarchy eh ON e.manager_id = eh.id
    )
    SELECT * FROM employee_hierarchy
    ORDER BY depth, id
''').fetchall()

print(result)