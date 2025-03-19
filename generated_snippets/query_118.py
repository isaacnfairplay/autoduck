# Generated: 2025-03-19 18:36:40.912395
# Result: [(1, datetime.datetime(2023, 6, 1, 10, 0), 22.5, 22.5), (1, datetime.datetime(2023, 6, 1, 11, 0), 23.100000381469727, 22.800000190734863), (2, datetime.datetime(2023, 6, 1, 10, 0), 21.799999237060547, 21.799999237060547), (2, datetime.datetime(2023, 6, 1, 11, 0), 22.299999237060547, 22.049999237060547)]
# Valid: True
import duckdb

# Create in-memory connection
conn = duckdb.connect(':memory:')

# Create a time series table with sensor data
conn.execute('''
    CREATE TABLE sensor_readings (
        timestamp TIMESTAMP,
        sensor_id INTEGER,
        temperature FLOAT
    );

    INSERT INTO sensor_readings VALUES
        ('2023-06-01 10:00:00', 1, 22.5),
        ('2023-06-01 11:00:00', 1, 23.1),
        ('2023-06-01 10:00:00', 2, 21.8),
        ('2023-06-01 11:00:00', 2, 22.3)
''');

# Compute rolling average temperature per sensor
result = conn.execute('''
    SELECT
        sensor_id,
        timestamp,
        temperature,
        AVG(temperature) OVER (
            PARTITION BY sensor_id
            ORDER BY timestamp
            ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
        ) as rolling_avg
    FROM sensor_readings
''').fetchall()

for row in result:
    print(f"Sensor {row[0]}: {row[1]} - Temp: {row[2]}, Rolling Avg: {row[3]:.2f}")