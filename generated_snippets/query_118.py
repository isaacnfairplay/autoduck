# Generated: 2025-03-19 12:23:10.478352
# Result: [('A', 'D', 'A->D', 2), ('A', 'D', 'A->D', 6), ('A', 'D', 'A->C->D', 5)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create graph network for path finding
conn.execute('''CREATE TABLE connections (
    start_node VARCHAR,
    end_node VARCHAR,
    distance INT
);''')

conn.execute('''
INSERT INTO connections VALUES
    ('A', 'B', 5),
    ('B', 'C', 3),
    ('A', 'C', 8),
    ('C', 'D', 2),
    ('B', 'D', 6)
''')

# Recursive query to find all possible paths
result = conn.execute('''
WITH RECURSIVE path_finder(start_node, end_node, path, total_distance) AS (
    SELECT start_node, end_node, start_node, 0
    FROM connections
    UNION ALL
    SELECT p.start_node, c.end_node, p.path || '->' || c.end_node, p.total_distance + c.distance
    FROM path_finder p
    JOIN connections c ON p.end_node = c.start_node
    WHERE c.end_node NOT LIKE '%' || p.path || '%'
)
SELECT * FROM path_finder
WHERE start_node = 'A' AND end_node = 'D'
''').fetchall()

for row in result:
    print(row)