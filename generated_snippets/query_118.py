# Generated: 2025-03-19 20:10:39.780462
# Result: [(1, datetime.datetime(2023, 6, 1, 10, 0), 22.5, 22.5), (1, datetime.datetime(2023, 6, 1, 10, 15), 23.100000381469727, 22.800000190734863), (2, datetime.datetime(2023, 6, 1, 10, 0), 19.799999237060547, 19.799999237060547), (2, datetime.datetime(2023, 6, 1, 10, 15), 20.200000762939453, 20.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table of sensor readings with time series data
conn.execute('''CREATE TABLE sensor_readings (
    device_id INTEGER,
    timestamp TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT
)''')

conn.execute('''INSERT INTO sensor_readings VALUES
    (1, '2023-06-01 10:00:00', 22.5, 45.3),
    (1, '2023-06-01 10:15:00', 23.1, 46.2),
    (2, '2023-06-01 10:00:00', 19.8, 55.7),
    (2, '2023-06-01 10:15:00', 20.2, 54.9)''')

# Calculate rolling temperature average per device
result = conn.execute('''
SELECT
    device_id,
    timestamp,
    temperature,
    AVG(temperature) OVER (
        PARTITION BY device_id
        ORDER BY timestamp
        ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
    ) AS rolling_temp_avg
FROM sensor_readings
ORDER BY device_id, timestamp
''').fetchall()

for row in result:
    print(f"Device: {row[0]}, Timestamp: {row[1]}, Temperature: {row[2]}, Rolling Avg: {row[3]}")