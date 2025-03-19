# Generated: 2025-03-19 14:31:13.785536
# Result: (datetime.datetime(2023, 1, 15, 10, 0), datetime.datetime(2023, 1, 15, 12, 0))
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create temporal data and demonstrate interval calculations
conn.execute("CREATE TABLE events (event_time TIMESTAMP, duration INTERVAL)")
conn.execute("INSERT INTO events VALUES ('2023-01-15 10:00:00', INTERVAL 2 HOURS)")

# Calculate end time using interval addition
result = conn.execute("""
    SELECT 
        event_time, 
        event_time + duration AS event_end_time
    FROM events
""").fetchone()

print(f"Start: {result[0]}, End: {result[1]}")