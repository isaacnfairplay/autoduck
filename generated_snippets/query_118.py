# Generated: 2025-03-19 20:26:05.674042
# Result: [(1, datetime.datetime(2023, 6, 1, 10, 0), 22.5, 0.09000011444125751), (1, datetime.datetime(2023, 6, 1, 11, 0), 23.100000381469727, 0.09000011444125751), (1, datetime.datetime(2023, 6, 1, 12, 0), 22.799999237060547, 0.09000011444125751), (2, datetime.datetime(2023, 6, 1, 10, 0), 21.700000762939453, 0.023333193461439805), (2, datetime.datetime(2023, 6, 1, 11, 0), 22.0, 0.023333193461439805), (2, datetime.datetime(2023, 6, 1, 12, 0), 21.899999618530273, 0.023333193461439805)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sensor temperature data
conn.execute('CREATE TABLE sensor_readings (sensor_id INT, timestamp TIMESTAMP, temperature FLOAT)')
conn.execute('''
INSERT INTO sensor_readings VALUES
    (1, '2023-06-01 10:00:00', 22.5),
    (1, '2023-06-01 11:00:00', 23.1),
    (1, '2023-06-01 12:00:00', 22.8),
    (2, '2023-06-01 10:00:00', 21.7),
    (2, '2023-06-01 11:00:00', 22.0),
    (2, '2023-06-01 12:00:00', 21.9)
''')

# Calculate temperature variance per sensor using window function
result = conn.execute('''
SELECT 
    sensor_id, 
    timestamp, 
    temperature,
    VARIANCE(temperature) OVER (PARTITION BY sensor_id) as temp_variance
FROM sensor_readings
''').fetchall()

for row in result:
    print(f"Sensor {row[0]}: Timestamp {row[1]}, Temp {row[2]}, Variance {row[3]:.2f}")