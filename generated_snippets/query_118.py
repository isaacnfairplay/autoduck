# Generated: 2025-03-19 11:38:03.427185
# Result: [(1, datetime.datetime(2023, 7, 1, 10, 0), 22.5, 0.18), (1, datetime.datetime(2023, 7, 1, 11, 0), 23.100000381469727, 0.18), (2, datetime.datetime(2023, 7, 1, 10, 0), 21.700000762939453, None)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sensor monitoring data
conn.execute('''
CREATE TABLE sensor_readings (
    timestamp TIMESTAMP,
    sensor_id INTEGER,
    temperature FLOAT,
    humidity FLOAT
);

INSERT INTO sensor_readings VALUES
('2023-07-01 10:00:00', 1, 22.5, 45.3),
('2023-07-01 11:00:00', 1, 23.1, 44.8),
('2023-07-01 10:00:00', 2, 21.7, 46.2);
''')

# Use window function to calculate sensor variance
result = conn.execute('''
SELECT
    sensor_id,
    timestamp,
    temperature,
    ROUND(VARIANCE(temperature) OVER (PARTITION BY sensor_id), 2) as temp_variance
FROM sensor_readings
''').fetchall()

for row in result:
    print(f"Sensor {row[0]} at {row[1]}: {row[2]}°C (Variance: {row[3]})")