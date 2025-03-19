# Generated: 2025-03-19 18:38:34.010797
# Result: [('Alice', 'HR', 0), ('Bob', 'Sales', 1), ('Charlie', 'Marketing', 1), ('David', 'Sales', 2)]
# Valid: True
import duckdb

# Create in-memory connection
conn = duckdb.connect(':memory:')

# Create a complex hierarchical data table
conn.execute('''
    CREATE TABLE organizational_hierarchy (
        employee_id INTEGER PRIMARY KEY,
        name VARCHAR,
        department VARCHAR,
        manager_id INTEGER
    );

    INSERT INTO organizational_hierarchy VALUES
        (1, 'Alice', 'HR', NULL),
        (2, 'Bob', 'Sales', 1),
        (3, 'Charlie', 'Marketing', 1),
        (4, 'David', 'Sales', 2);
''');

# Use recursive common table expression to traverse hierarchy
result = conn.execute('''
    WITH RECURSIVE hierarchy_traversal AS (
        SELECT employee_id, name, department, manager_id, 0 as depth
        FROM organizational_hierarchy
        WHERE manager_id IS NULL

        UNION ALL

        SELECT 
            o.employee_id, 
            o.name, 
            o.department, 
            o.manager_id, 
            h.depth + 1
        FROM organizational_hierarchy o
        JOIN hierarchy_traversal h ON o.manager_id = h.employee_id
    )
    SELECT name, department, depth
    FROM hierarchy_traversal
    ORDER BY depth, name
''').fetchall()

for row in result:
    print(f"Name: {row[0]}, Department: {row[1]}, Hierarchy Depth: {row[2]})")