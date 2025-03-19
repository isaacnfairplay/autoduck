# Generated: 2025-03-19 09:33:55.298834
# Result: [(1, 'login', datetime.datetime(2023, 6, 1, 10, 0), 'purchase'), (1, 'purchase', datetime.datetime(2023, 6, 1, 11, 30), None), (2, 'login', datetime.datetime(2023, 6, 2, 15, 45), 'view'), (2, 'view', datetime.datetime(2023, 6, 2, 16, 0), None)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample table of user events
conn.sql("""
CREATE TABLE user_events (
    user_id INTEGER,
    event_type VARCHAR,
    timestamp TIMESTAMP
);

INSERT INTO user_events VALUES
    (1, 'login', '2023-06-01 10:00:00'),
    (1, 'purchase', '2023-06-01 11:30:00'),
    (2, 'login', '2023-06-02 15:45:00'),
    (2, 'view', '2023-06-02 16:00:00')
""")

# Demonstrate temporal event sequence analysis
result = conn.sql("""
SELECT
    user_id,
    event_type,
    timestamp,
    LEAD(event_type) OVER (PARTITION BY user_id ORDER BY timestamp) as next_event
FROM user_events
""").fetchall()

print(result)