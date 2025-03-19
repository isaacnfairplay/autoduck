# Generated: 2025-03-19 17:53:03.409960
# Result: [(5,), (2,), (1,), (3,), (4,)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate recursive graph data
conn.execute('''CREATE TABLE graph_edges (
    source INTEGER,
    destination INTEGER
)''')

conn.executemany('INSERT INTO graph_edges VALUES (?, ?)', [
    (1, 2), (2, 3), (3, 4), (1, 4), (4, 5)
])

# Use recursive CTE to find all reachable nodes from node 1
result = conn.execute('''
WITH RECURSIVE path_search(node) AS (
    SELECT source FROM graph_edges WHERE source = 1
    UNION
    SELECT e.destination
    FROM graph_edges e
    JOIN path_search ps ON e.source = ps.node
)
SELECT DISTINCT node FROM path_search
''').fetchall()

print(result)  # Will show reachable nodes from node 1