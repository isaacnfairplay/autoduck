# Generated: 2025-03-19 21:02:34.800577
# Result: [(1, datetime.datetime(2023, 7, 1, 10, 0), 22.5, 22.5), (1, datetime.datetime(2023, 7, 1, 10, 15), 23.100000381469727, 22.800000190734863), (1, datetime.datetime(2023, 7, 1, 10, 30), 22.799999237060547, 22.949999809265137), (2, datetime.datetime(2023, 7, 1, 10, 0), 21.700000762939453, 21.700000762939453)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample time series data
conn.sql('''
CREATE TABLE sensor_readings (
    timestamp TIMESTAMP,
    device_id INTEGER,
    temperature FLOAT
);

INSERT INTO sensor_readings VALUES
('2023-07-01 10:00:00', 1, 22.5),
('2023-07-01 10:15:00', 1, 23.1),
('2023-07-01 10:30:00', 1, 22.8),
('2023-07-01 10:00:00', 2, 21.7);
''')

# Use window functions for time-based analysis
result = conn.sql('''
SELECT
    device_id,
    timestamp,
    temperature,
    AVG(temperature) OVER (PARTITION BY device_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as rolling_avg
FROM sensor_readings
''').fetchall()

print(result)