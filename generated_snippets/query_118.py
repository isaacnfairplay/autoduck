# Generated: 2025-03-19 12:19:40.223717
# Result: [(1, datetime.datetime(2023, 6, 1, 10, 0), Decimal('22.50'), 22.5), (1, datetime.datetime(2023, 6, 1, 11, 0), Decimal('23.10'), 22.8), (2, datetime.datetime(2023, 6, 1, 10, 0), Decimal('21.80'), 21.8), (2, datetime.datetime(2023, 6, 1, 11, 0), Decimal('22.30'), 22.05)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate a time series sensor data table
conn.execute('''CREATE TABLE sensor_readings (
    sensor_id INT,
    timestamp TIMESTAMP,
    temperature DECIMAL(5,2),
    humidity DECIMAL(5,2)
);''')

conn.execute('''
INSERT INTO sensor_readings VALUES
    (1, '2023-06-01 10:00:00', 22.5, 45.3),
    (1, '2023-06-01 11:00:00', 23.1, 46.2),
    (2, '2023-06-01 10:00:00', 21.8, 44.7),
    (2, '2023-06-01 11:00:00', 22.3, 45.5)
''')

# Perform time-based moving average with window function
result = conn.execute('''
SELECT
    sensor_id,
    timestamp,
    temperature,
    AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg_temp
FROM sensor_readings
''').fetchall()

for row in result:
    print(row)