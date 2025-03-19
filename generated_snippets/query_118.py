# Generated: 2025-03-19 11:01:25.529939
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create employee hierarchy table
conn.execute('''
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name VARCHAR,
    manager_id INTEGER
);

INSERT INTO employees VALUES
    (1, 'CEO', NULL),
    (2, 'CTO', 1),
    (3, 'CFO', 1),
    (4, 'Senior Engineer', 2),
    (5, 'Junior Engineer', 4);

-- Recursive CTE to trace organizational hierarchy
WITH RECURSIVE org_hierarchy AS (
    SELECT employee_id, name, manager_id, 0 AS depth
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT e.employee_id, e.name, e.manager_id, oh.depth + 1
    FROM employees e
    JOIN org_hierarchy oh ON e.manager_id = oh.employee_id
)

SELECT * FROM org_hierarchy ORDER BY depth, employee_id;
''').fetchall()