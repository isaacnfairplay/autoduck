# Generated: 2025-03-19 11:25:54.988583
# Result: [(1, datetime.datetime(2023, 6, 1, 10, 0), 22.5, 22.5), (1, datetime.datetime(2023, 6, 1, 11, 0), 23.100000381469727, 22.800000190734863), (1, datetime.datetime(2023, 6, 1, 12, 0), 23.799999237060547, 23.449999809265137), (2, datetime.datetime(2023, 6, 1, 10, 0), 21.700000762939453, 21.700000762939453)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time series data
conn.execute('''
CREATE TABLE temperature_readings (
    timestamp TIMESTAMP,
    sensor_id INTEGER,
    temperature FLOAT
);

INSERT INTO temperature_readings VALUES
('2023-06-01 10:00:00', 1, 22.5),
('2023-06-01 11:00:00', 1, 23.1),
('2023-06-01 12:00:00', 1, 23.8),
('2023-06-01 10:00:00', 2, 21.7);
''')

# Calculate moving average with window function
result = conn.execute('''
SELECT 
    sensor_id, 
    timestamp, 
    temperature,
    AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg
FROM temperature_readings
''').fetchall()

for row in result:
    print(f"Sensor {row[0]} at {row[1]}: {row[2]}°C (Moving Avg: {row[3]:.2f}°C)")