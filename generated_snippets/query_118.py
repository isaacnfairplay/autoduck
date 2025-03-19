# Generated: 2025-03-19 16:18:08.044272
# Result: [(1, Decimal('100.50'), datetime.date(2023, 1, 15), Decimal('100.50')), (1, Decimal('250.75'), datetime.date(2023, 2, 20), Decimal('351.25')), (2, Decimal('75.25'), datetime.date(2023, 3, 10), Decimal('75.25')), (2, Decimal('125.00'), datetime.date(2023, 4, 5), Decimal('200.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate hierarchical data processing with recursive CTE
conn.execute('''
    CREATE TABLE org_hierarchy (
        employee_id INT,
        name VARCHAR,
        manager_id INT
    );

    INSERT INTO org_hierarchy VALUES
        (1, 'CEO', NULL),
        (2, 'VP Engineering', 1),
        (3, 'VP Sales', 1),
        (4, 'Engineering Manager', 2),
        (5, 'Sales Manager', 3);

    WITH RECURSIVE employee_path AS (
        SELECT 
            employee_id, 
            name, 
            manager_id,
            CAST(name AS VARCHAR) AS hierarchy_path
        FROM org_hierarchy WHERE manager_id IS NULL

        UNION ALL

        SELECT 
            e.employee_id, 
            e.name, 
            e.manager_id,
            ep.hierarchy_path || ' -> ' || e.name
        FROM org_hierarchy e
        JOIN employee_path ep ON e.manager_id = ep.employee_id
    )
    SELECT * FROM employee_path
''').fetchall()