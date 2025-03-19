# Generated: 2025-03-19 15:01:20.588321
# Result: <duckdb.duckdb.DuckDBPyConnection object at 0x00000147DE9344F0>
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with sensor readings
conn.execute('''CREATE TABLE sensor_data (
    sensor_id INTEGER,
    reading FLOAT,
    timestamp TIMESTAMP
)''')

# Insert sample sensor data
conn.execute('''INSERT INTO sensor_data VALUES
    (1, 22.5, '2023-07-01 10:00:00'),
    (1, 23.1, '2023-07-01 10:15:00'),
    (1, 22.8, '2023-07-01 10:30:00'),
    (2, 18.6, '2023-07-01 10:00:00'),
    (2, 19.2, '2023-07-01 10:15:00')''')

# Use window functions to calculate moving average of sensor readings
result = conn.execute('''SELECT 
    sensor_id, 
    reading, 
    timestamp,
    AVG(reading) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS moving_avg
FROM sensor_data''')

print(result.fetchall())