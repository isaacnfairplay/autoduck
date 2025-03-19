# Generated: 2025-03-19 18:25:31.621576
# Result: (2, datetime.datetime(2023, 6, 15, 10, 15), Decimal('22.30'), 22.05)
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sensor temperature data
conn.execute('''
CREATE TABLE sensor_readings (
    sensor_id INTEGER,
    temperature DECIMAL(5,2),
    timestamp TIMESTAMP
);

INSERT INTO sensor_readings VALUES
    (1, 22.5, '2023-06-15 10:00:00'),
    (1, 23.1, '2023-06-15 10:15:00'),
    (2, 21.8, '2023-06-15 10:00:00'),
    (2, 22.3, '2023-06-15 10:15:00');
'''
)

# Calculate moving average of temperatures per sensor
query = '''
SELECT 
    sensor_id, 
    timestamp,
    temperature,
    AVG(temperature) OVER (
        PARTITION BY sensor_id 
        ORDER BY timestamp 
        ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
    ) as moving_avg
FROM sensor_readings
ORDER BY sensor_id, timestamp;
'''

results = conn.execute(query).fetchall()
for result in results:
    print(result)