# Generated: 2025-03-19 13:50:20.114064
# Result: [(1, datetime.datetime(2023, 5, 1, 10, 0), 22.5, 22.5), (1, datetime.datetime(2023, 5, 1, 11, 0), 23.100000381469727, 22.800000190734863), (2, datetime.datetime(2023, 5, 1, 10, 0), 21.700000762939453, 21.700000762939453), (2, datetime.datetime(2023, 5, 1, 11, 0), 22.299999237060547, 22.0)]
# Valid: True
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create table with sensor temperature data
conn.execute('''
CREATE TABLE sensor_readings (
    sensor_id INTEGER,
    timestamp TIMESTAMP,
    temperature FLOAT
)''')

# Insert sample sensor readings
conn.execute('''
INSERT INTO sensor_readings VALUES
    (1, '2023-05-01 10:00:00', 22.5),
    (1, '2023-05-01 11:00:00', 23.1),
    (2, '2023-05-01 10:00:00', 21.7),
    (2, '2023-05-01 11:00:00', 22.3)
''')

# Calculate moving average temperature for each sensor
result = conn.execute('''
SELECT 
    sensor_id, 
    timestamp, 
    temperature,
    AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg
FROM sensor_readings
''').fetchall()

print(result)