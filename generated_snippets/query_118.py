# Generated: 2025-03-19 19:01:40.394517
# Result: [(1, 'click', datetime.datetime(2023, 7, 15, 10, 30), 1), (1, 'purchase', datetime.datetime(2023, 7, 15, 11, 15), 2), (2, 'view', datetime.datetime(2023, 7, 15, 9, 45), 1), (2, 'click', datetime.datetime(2023, 7, 15, 10, 0), 2)]
# Valid: True
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create user interactions table
conn.sql('''
CREATE TABLE user_interactions (
    user_id INTEGER,
    interaction_type VARCHAR,
    timestamp TIMESTAMP
);

INSERT INTO user_interactions VALUES
    (1, 'click', '2023-07-15 10:30:00'),
    (1, 'purchase', '2023-07-15 11:15:00'),
    (2, 'view', '2023-07-15 09:45:00'),
    (2, 'click', '2023-07-15 10:00:00');
''')

# Use window function to rank user interactions
result = conn.sql('''
SELECT 
    user_id, 
    interaction_type,
    timestamp,
    RANK() OVER (PARTITION BY user_id ORDER BY timestamp) as interaction_rank
FROM user_interactions
ORDER BY user_id, interaction_rank
''').fetchall()

for row in result:
    print(f"User {row[0]}: {row[1]} at {row[2]}, Rank: {row[3]}")