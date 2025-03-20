# Generated: 2025-03-19 20:42:33.187787
# Result: [(1, datetime.datetime(2023, 6, 15, 10, 0), Decimal('22.50'), 0.0), (1, datetime.datetime(2023, 6, 15, 10, 15), Decimal('23.10'), 0.3000000000000007), (2, datetime.datetime(2023, 6, 15, 10, 0), Decimal('21.70'), 0.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sensors table for time series data
conn.execute('''
CREATE TABLE sensor_readings (
    sensor_id INTEGER,
    timestamp TIMESTAMP,
    temperature DECIMAL(5,2),
    humidity DECIMAL(5,2)
);''')

# Insert sample sensor data
conn.executemany('INSERT INTO sensor_readings VALUES (?, ?, ?, ?)', [
    (1, '2023-06-15 10:00:00', 22.5, 45.3),
    (1, '2023-06-15 10:15:00', 23.1, 46.0),
    (2, '2023-06-15 10:00:00', 21.7, 42.8)
])

# Use window functions to calculate temperature change
result = conn.execute('''
SELECT 
    sensor_id, 
    timestamp,
    temperature,
    temperature - AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as temp_deviation
FROM sensor_readings
''').fetchall()

print(result)