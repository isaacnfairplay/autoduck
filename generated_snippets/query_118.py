# Generated: 2025-03-19 21:31:21.377145
# Result: [(1, datetime.datetime(2023, 6, 15, 10, 0), 22.5, 22.5), (1, datetime.datetime(2023, 6, 15, 11, 0), 23.100000381469727, 22.800000190734863), (2, datetime.datetime(2023, 6, 15, 10, 0), 19.799999237060547, 19.799999237060547), (2, datetime.datetime(2023, 6, 15, 11, 0), 20.200000762939453, 20.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table of sensor readings
conn.execute('''
CREATE TABLE sensor_data (
    sensor_id INT,
    reading_timestamp TIMESTAMP,
    temperature FLOAT
)''')

# Insert sample sensor data
conn.executemany('INSERT INTO sensor_data VALUES (?, ?, ?)', [
    (1, '2023-06-15 10:00:00', 22.5),
    (1, '2023-06-15 11:00:00', 23.1),
    (2, '2023-06-15 10:00:00', 19.8),
    (2, '2023-06-15 11:00:00', 20.2)
])

# Calculate moving average of temperature per sensor
result = conn.sql('''
SELECT 
    sensor_id, 
    reading_timestamp, 
    temperature,
    AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY reading_timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg
FROM sensor_data
''').fetchall()

print(result)