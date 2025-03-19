# Generated: 2025-03-19 10:56:58.315252
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create employee hierarchy table
conn.execute('''
    CREATE TABLE employees (
        employee_id INT,
        name TEXT,
        manager_id INT
    );

    INSERT INTO employees VALUES
        (1, 'CEO', NULL),
        (2, 'VP Sales', 1),
        (3, 'VP Tech', 1),
        (4, 'Sales Manager', 2),
        (5, 'Tech Manager', 3);

    WITH RECURSIVE hierarchy AS (
        SELECT employee_id, name, manager_id, 0 AS depth
        FROM employees WHERE manager_id IS NULL

        UNION ALL

        SELECT e.employee_id, e.name, e.manager_id, h.depth + 1
        FROM employees e
        JOIN hierarchy h ON e.manager_id = h.employee_id
    )
    SELECT * FROM hierarchy
''').fetchall()