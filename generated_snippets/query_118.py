# Generated: 2025-03-19 19:15:17.064316
# Result: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a graph-like dataset of users and connections
conn.sql("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name VARCHAR
);

CREATE TABLE connections (
    user_id INTEGER,
    connected_user_id INTEGER
);

INSERT INTO users VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'David');

INSERT INTO connections VALUES
(1, 2), (1, 3),
(2, 1), (2, 4),
(3, 1), (4, 2);

-- Demonstrate recursive query to find network connections
WITH RECURSIVE network(user_id, depth) AS (
    SELECT user_id, 0 FROM users WHERE name = 'Alice'
    UNION ALL
    SELECT c.connected_user_id, n.depth + 1
    FROM connections c
    JOIN network n ON c.user_id = n.user_id
    WHERE depth < 2
)
SELECT DISTINCT u.name, network.depth
FROM network
JOIN users u ON network.user_id = u.user_id;
""").show()