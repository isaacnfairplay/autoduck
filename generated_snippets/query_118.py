# Generated: 2025-03-19 20:18:29.268517
# Result: [('Alice', 'Bob', 1), ('Charlie', 'David', 1), ('Alice', 'Charlie', 1), ('Bob', 'Charlie', 1), ('Alice', 'David', 2), ('Alice', 'Charlie', 2), ('Bob', 'David', 2), ('Alice', 'David', 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and query a graph-like social network relationship network
conn.execute('''CREATE TABLE users (user_id INT, name VARCHAR)''')
conn.execute('''CREATE TABLE connections (user1_id INT, user2_id INT)''')

conn.execute('''INSERT INTO users VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie'), (4, 'David')''')
conn.execute('''INSERT INTO connections VALUES (1, 2), (1, 3), (2, 3), (3, 4)''')

# Find mutual connections using recursive CTE
result = conn.execute('''
WITH RECURSIVE connection_paths AS (
    SELECT user1_id, user2_id, 1 as path_length
    FROM connections
    UNION ALL
    SELECT cp.user1_id, c.user2_id, cp.path_length + 1
    FROM connection_paths cp
    JOIN connections c ON cp.user2_id = c.user1_id
    WHERE cp.path_length < 3
)
SELECT DISTINCT u1.name, u2.name, path_length
FROM connection_paths cp
JOIN users u1 ON cp.user1_id = u1.user_id
JOIN users u2 ON cp.user2_id = u2.user_id
ORDER BY path_length
''').fetchall()

for row in result:
    print(f"Connection: {row[0]} -> {row[1]} (Path Length: {row[2]})")