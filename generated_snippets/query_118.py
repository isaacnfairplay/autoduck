# Generated: 2025-03-19 13:54:38.556552
# Result: <duckdb.duckdb.DuckDBPyConnection object at 0x00000147DE994530>
# Valid: True
import duckdb

# Connect to memory database
conn = duckdb.connect(':memory:')

# Create table with recursive employee hierarchy
conn.execute('''CREATE TABLE employees (
    emp_id INTEGER,
    name VARCHAR,
    manager_id INTEGER
)''')

# Insert hierarchical employee data
conn.execute('''INSERT INTO employees VALUES
    (1, 'CEO', NULL),
    (2, 'CTO', 1),
    (3, 'CFO', 1),
    (4, 'Senior Engineer', 2),
    (5, 'Junior Engineer', 4)''')

# Use recursive CTE to trace management chain
result = conn.execute('''WITH RECURSIVE management_chain AS (
    SELECT emp_id, name, manager_id, 0 as depth
    FROM employees WHERE emp_id = 5
    UNION ALL
    SELECT e.emp_id, e.name, e.manager_id, mc.depth + 1
    FROM employees e
    JOIN management_chain mc ON e.emp_id = mc.manager_id
)
SELECT name, depth FROM management_chain ORDER BY depth''')

print(result.fetchall())