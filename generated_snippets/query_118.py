# Generated: 2025-03-19 15:16:52.923171
# Result: [('login', datetime.datetime(2023, 1, 1, 10, 0), 100, None, 100), ('purchase', datetime.datetime(2023, 1, 1, 11, 0), 250, 100, 100), ('login', datetime.datetime(2023, 1, 2, 9, 0), 75, 250, 75), ('logout', datetime.datetime(2023, 1, 2, 14, 0), 50, 75, 75)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate temporal data processing with date window functions
conn.execute('CREATE TABLE events (timestamp TIMESTAMP, event_type VARCHAR, value INT)')
conn.execute("""INSERT INTO events VALUES
    ('2023-01-01 10:00:00', 'login', 100),
    ('2023-01-01 11:00:00', 'purchase', 250),
    ('2023-01-02 09:00:00', 'login', 75),
    ('2023-01-02 14:00:00', 'logout', 50)
""")

result = conn.execute('''
    SELECT 
        event_type, 
        timestamp, 
        value,
        LAG(value) OVER (ORDER BY timestamp) as previous_value,
        FIRST_VALUE(value) OVER (PARTITION BY DATE_TRUNC('day', timestamp)) as first_daily_value
    FROM events
''').fetchall()

print(result)