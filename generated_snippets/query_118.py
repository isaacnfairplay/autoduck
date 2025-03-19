# Generated: 2025-03-19 15:35:03.028149
# Result: [('Senior Developer', 0), ('Engineering Manager', 1), ('VP Engineering', 2), ('CEO', 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate hierarchical data querying with recursive Common Table Expression
result = conn.sql("""
WITH RECURSIVE organizational_hierarchy(id, name, manager_id) AS (
    SELECT 1, 'CEO', NULL
    UNION ALL
    SELECT 2, 'VP Engineering', 1
    UNION ALL
    SELECT 3, 'Engineering Manager', 2
    UNION ALL
    SELECT 4, 'Senior Developer', 3
),
reporting_chain AS (
    SELECT id, name, manager_id, 0 as depth
    FROM organizational_hierarchy WHERE name = 'Senior Developer'
    UNION ALL
    SELECT o.id, o.name, o.manager_id, rc.depth + 1
    FROM organizational_hierarchy o
    JOIN reporting_chain rc ON o.id = rc.manager_id
)
SELECT name, depth FROM reporting_chain ORDER BY depth
""").fetchall()

print(result)  # Will show reporting chain from Senior Developer up