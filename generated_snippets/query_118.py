# Generated: 2025-03-19 13:08:28.283314
# Result: [(1, 'view', datetime.datetime(2023, 6, 15, 10, 15), None), (1, 'click', datetime.datetime(2023, 6, 15, 10, 16), 'view'), (2, 'view', datetime.datetime(2023, 6, 15, 11, 20), None), (2, 'purchase', datetime.datetime(2023, 6, 15, 11, 22), 'view')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate a table of user interactions
conn.execute('''CREATE TABLE interactions (
    user_id INT,
    interaction_type VARCHAR,
    timestamp TIMESTAMP
)''')

conn.execute('''INSERT INTO interactions VALUES
    (1, 'view', '2023-06-15 10:15:00'),
    (1, 'click', '2023-06-15 10:16:00'),
    (2, 'view', '2023-06-15 11:20:00'),
    (2, 'purchase', '2023-06-15 11:22:00')
''')

# Demonstrate consecutive event tracking using window functions
result = conn.execute('''SELECT
    user_id,
    interaction_type,
    timestamp,
    LAG(interaction_type) OVER (PARTITION BY user_id ORDER BY timestamp) as prev_interaction
FROM interactions
''').fetchall()

for row in result:
    print(row)