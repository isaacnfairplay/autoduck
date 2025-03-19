# Generated: 2025-03-19 17:35:08.730216
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

# Demonstrating hierarchical data processing with recursive CTEs
conn = duckdb.connect(':memory:')

# Create an employee hierarchy table
conn.sql("""
CREATE TABLE employees (
    id INTEGER,
    name VARCHAR,
    manager_id INTEGER
);

INSERT INTO employees VALUES
(1, 'Alice', NULL),
(2, 'Bob', 1),
(3, 'Charlie', 1),
(4, 'David', 2),
(5, 'Eve', 3);

-- Recursive CTE to find all subordinates
WITH RECURSIVE subordinate_chain AS (
    SELECT id, name, manager_id, 0 AS depth
    FROM employees
    WHERE name = 'Alice'

    UNION ALL

    SELECT e.id, e.name, e.manager_id, sc.depth + 1
    FROM employees e
    JOIN subordinate_chain sc ON e.manager_id = sc.id
)
SELECT name, depth
FROM subordinate_chain
""").show()