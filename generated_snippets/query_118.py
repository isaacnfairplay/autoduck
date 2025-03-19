# Generated: 2025-03-19 17:59:59.945094
# Result: [(datetime.datetime(2023, 1, 1, 10, 0), datetime.datetime(2023, 1, 1, 12, 0), datetime.timedelta(seconds=7200))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create temporal data and calculate time differences
conn.execute('CREATE TABLE events (event_time TIMESTAMP, duration INTERVAL)')
conn.execute("INSERT INTO events VALUES ('2023-01-01 10:00:00', INTERVAL 2 HOURS)")

result = conn.execute("""
    SELECT 
        event_time, 
        event_time + duration AS end_time,
        duration
    FROM events
""").fetchall()

print(result)  # Demonstrates timestamp and interval manipulation