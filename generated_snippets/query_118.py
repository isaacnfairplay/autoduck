# Generated: 2025-03-19 13:07:36.122673
# Result: [(1, datetime.datetime(2023, 1, 1, 10, 15), 22.5, 22.5), (1, datetime.datetime(2023, 1, 1, 10, 20), 23.100000381469727, 22.800000190734863), (1, datetime.datetime(2023, 1, 1, 10, 25), 22.799999237060547, 22.949999809265137), (2, datetime.datetime(2023, 1, 1, 10, 15), 24.0, 24.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create temporal data for complex time-based query
conn.execute('''
CREATE TABLE events (
    event_time TIMESTAMP,
    sensor_id INTEGER,
    temperature FLOAT
)''')

conn.execute('''
INSERT INTO events VALUES
    ('2023-01-01 10:15:00', 1, 22.5),
    ('2023-01-01 10:20:00', 1, 23.1),
    ('2023-01-01 10:25:00', 1, 22.8),
    ('2023-01-01 10:15:00', 2, 24.0)
''')

# Demonstrate time-based window function with moving average
result = conn.execute('''
SELECT 
    sensor_id, 
    event_time,
    temperature,
    AVG(temperature) OVER (
        PARTITION BY sensor_id 
        ORDER BY event_time 
        ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
    ) as rolling_temp
FROM events
''').fetchall()

for row in result:
    print(row)