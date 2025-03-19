# Generated: 2025-03-19 14:26:00.279194
# Result: [(datetime.datetime(2023, 6, 15, 1, 0), 1, 22.5, 22.5), (datetime.datetime(2023, 6, 15, 2, 0), 1, 21.799999237060547, 22.149999618530273), (datetime.datetime(2023, 6, 15, 3, 0), 1, 21.200000762939453, 21.833333333333332), (datetime.datetime(2023, 6, 15, 4, 0), 1, 20.899999618530273, 21.299999872843426)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a time series table with hourly temperatures
conn.execute('CREATE TABLE temperature_log (timestamp TIMESTAMP, sensor_id INT, temperature FLOAT)')
conn.execute('''
INSERT INTO temperature_log VALUES
    ('2023-06-15 01:00:00', 1, 22.5),
    ('2023-06-15 02:00:00', 1, 21.8),
    ('2023-06-15 03:00:00', 1, 21.2),
    ('2023-06-15 04:00:00', 1, 20.9)
''')

# Calculate moving average of temperature with 3-hour window
result = conn.execute('''
SELECT 
    timestamp, 
    sensor_id, 
    temperature,
    AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg
FROM temperature_log
''').fetchall()

for row in result:
    print(row)