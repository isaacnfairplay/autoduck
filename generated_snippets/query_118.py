# Generated: 2025-03-19 09:13:19.947029
# Result: [(1, 'Click', datetime.datetime(2023, 7, 15, 10, 0), 3, 'Click'), (1, 'Purchase', datetime.datetime(2023, 7, 15, 11, 30), 3, 'Click'), (1, 'Search', datetime.datetime(2023, 7, 15, 13, 45), 3, 'Click'), (2, 'View', datetime.datetime(2023, 7, 15, 12, 15), 1, 'View')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create user interactions tracking table
conn.execute('CREATE TABLE user_interactions (user_id INT, interaction_type TEXT, timestamp TIMESTAMP)')

# Insert sample interaction data
conn.executemany('INSERT INTO user_interactions VALUES (?, ?, ?)', [
    (1, 'Click', '2023-07-15 10:00:00'),
    (1, 'Purchase', '2023-07-15 11:30:00'),
    (2, 'View', '2023-07-15 12:15:00'),
    (1, 'Search', '2023-07-15 13:45:00')
])

# Analyze user interactions with advanced window functions
result = conn.execute('''SELECT
    user_id,
    interaction_type,
    timestamp,
    COUNT(*) OVER (PARTITION BY user_id) as total_interactions,
    FIRST_VALUE(interaction_type) OVER (PARTITION BY user_id ORDER BY timestamp) as first_interaction
FROM user_interactions
''').fetchall()

for row in result:
    print(f"User ID: {row[0]}, Type: {row[1]}, Time: {row[2]}, Total Interactions: {row[3]}, First Interaction: {row[4]}")