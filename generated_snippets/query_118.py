# Generated: 2025-03-19 11:07:36.301401
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create complex organizational hierarchy
conn.execute('''
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name VARCHAR,
    manager_id INTEGER,
    salary DECIMAL(10,2)
);

INSERT INTO employees VALUES
    (1, 'Alice', NULL, 150000),
    (2, 'Bob', 1, 100000),
    (3, 'Charlie', 1, 95000),
    (4, 'David', 2, 75000),
    (5, 'Eve', 2, 70000);

-- Recursive hierarchy with salary aggregation
WITH RECURSIVE org_hierarchy(employee_id, name, manager_id, level, total_team_salary) AS (
    SELECT 
        employee_id, 
        name, 
        manager_id, 
        0 AS level, 
        salary AS total_team_salary
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT 
        e.employee_id, 
        e.name, 
        e.manager_id, 
        oh.level + 1, 
        oh.total_team_salary + e.salary
    FROM employees e
    JOIN org_hierarchy oh ON e.manager_id = oh.employee_id
)

SELECT * FROM org_hierarchy ORDER BY level, employee_id;''').fetchall()