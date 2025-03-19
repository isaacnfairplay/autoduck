# Generated: 2025-03-19 09:56:14.202402
# Result: [(3, 'Electronics', Decimal('1200.00'), 1), (1, 'Electronics', Decimal('500.50'), 2), (4, 'Books', Decimal('75.25'), 1), (2, 'Clothing', Decimal('250.75'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create employee hierarchy table
conn.execute('''
CREATE TABLE employees (
    employee_id INT,
    name VARCHAR,
    manager_id INT
);

INSERT INTO employees VALUES
(1, 'CEO', NULL),
(2, 'CTO', 1),
(3, 'CFO', 1),
(4, 'Engineering Manager', 2),
(5, 'Sales Manager', 3),
(6, 'Engineer', 4),
(7, 'Sales Rep', 5);

WITH RECURSIVE employee_hierarchy AS (
    SELECT employee_id, name, manager_id, 1 AS depth
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.name, e.manager_id, eh.depth + 1
    FROM employees e
    JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id
)
SELECT * FROM employee_hierarchy;
''').fetchall()