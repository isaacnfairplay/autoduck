# Generated: 2025-03-19 18:57:18.232781
# Result: [(1, datetime.datetime(2023, 6, 1, 10, 0), 22.5, 22.5), (1, datetime.datetime(2023, 6, 1, 11, 0), 23.100000381469727, 22.800000190734863), (2, datetime.datetime(2023, 6, 1, 10, 0), 21.799999237060547, 21.799999237060547), (2, datetime.datetime(2023, 6, 1, 11, 0), 22.299999237060547, 22.049999237060547)]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create and populate temperature sensor data
conn.sql("""
CREATE TABLE sensor_readings (
    sensor_id INTEGER,
    timestamp TIMESTAMP,
    temperature FLOAT
);

INSERT INTO sensor_readings VALUES
    (1, '2023-06-01 10:00:00', 22.5),
    (1, '2023-06-01 11:00:00', 23.1),
    (2, '2023-06-01 10:00:00', 21.8),
    (2, '2023-06-01 11:00:00', 22.3);
""")

# Calculate moving average temperature per sensor
result = conn.sql("""
SELECT 
    sensor_id, 
    timestamp, 
    temperature,
    AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as rolling_avg
FROM sensor_readings
""").fetchall()

for row in result:
    print(f"Sensor {row[0]}: {row[1]} - Temp: {row[2]}°C, Rolling Avg: {row[3]}°C")