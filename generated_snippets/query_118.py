# Generated: 2025-03-19 12:14:12.431209
# Result: [(1, Decimal('22.50'), datetime.datetime(2023, 7, 15, 10, 0), 22.5), (1, Decimal('23.10'), datetime.datetime(2023, 7, 15, 10, 15), 22.8), (2, Decimal('21.80'), datetime.datetime(2023, 7, 15, 10, 0), 21.8), (2, Decimal('22.30'), datetime.datetime(2023, 7, 15, 10, 15), 22.05)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with sensor temperature readings
conn.execute('CREATE TABLE temperature_readings (sensor_id INT, reading DECIMAL(5,2), timestamp TIMESTAMP)')
conn.executemany('INSERT INTO temperature_readings VALUES (?, ?, ?)', [
    (1, 22.5, '2023-07-15 10:00:00'),
    (1, 23.1, '2023-07-15 10:15:00'),
    (2, 21.8, '2023-07-15 10:00:00'),
    (2, 22.3, '2023-07-15 10:15:00')
])

# Use window function to calculate rolling average temperature per sensor
result = conn.execute('''
    SELECT 
        sensor_id, 
        reading, 
        timestamp,
        AVG(reading) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as rolling_avg
    FROM temperature_readings
''').fetchall()

print(result)