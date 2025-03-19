# Generated: 2025-03-19 11:42:30.538787
# Result: [(datetime.datetime(2023, 7, 1, 10, 0), 1, 22.5, 0.3000001907348633), (datetime.datetime(2023, 7, 1, 11, 0), 1, 23.100000381469727, 7.366666158040363), (datetime.datetime(2023, 7, 1, 12, 0), 1, 45.79999923706055, 11.34999942779541)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create temperature tracking table with anomaly detection
conn.execute('''CREATE TABLE temperature_log (
    timestamp TIMESTAMP,
    sensor_id INTEGER,
    temperature FLOAT
);

INSERT INTO temperature_log VALUES
('2023-07-01 10:00:00', 1, 22.5),
('2023-07-01 11:00:00', 1, 23.1),
('2023-07-01 12:00:00', 1, 45.8);
''')

# Detect temperature anomalies using window function
result = conn.execute('''
SELECT 
    timestamp,
    sensor_id,
    temperature,
    ABS(temperature - AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)) as temp_deviation
FROM temperature_log
''').fetchall()

for row in result:
    print(f"Sensor {row[1]} at {row[0]}: {row[2]}°C (Deviation: {row[3]:.2f}°C)")