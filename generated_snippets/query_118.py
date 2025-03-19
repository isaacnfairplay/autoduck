# Generated: 2025-03-19 13:22:53.501766
# Result: [(datetime.date(2023, 1, 15), datetime.datetime(2023, 1, 17, 0, 0), 172800.0), (datetime.date(2023, 2, 20), datetime.datetime(2023, 2, 27, 0, 0), 604800.0), (datetime.date(2023, 3, 25), datetime.datetime(2023, 3, 25, 3, 0), 10800.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate temporal date functions and interval calculations
conn.execute('''CREATE TABLE events (
    event_date DATE,
    duration INTERVAL
)''')

conn.execute('''INSERT INTO events VALUES
    ('2023-01-15', INTERVAL 2 DAYS),
    ('2023-02-20', INTERVAL 1 WEEK),
    ('2023-03-25', INTERVAL 3 HOURS)''')

result = conn.execute('''
SELECT 
    event_date, 
    event_date + duration AS end_date,
    EXTRACT(EPOCH FROM duration) AS duration_seconds
FROM events
''').fetchall()

for row in result:
    print(f"Start: {row[0]}, End: {row[1]}, Duration: {row[2]} seconds")