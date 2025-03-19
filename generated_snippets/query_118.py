# Generated: 2025-03-19 16:51:18.992899
# Result: [(1, datetime.datetime(2023, 6, 1, 10, 0), 22.5, 22.5), (1, datetime.datetime(2023, 6, 1, 11, 0), 23.100000381469727, 22.800000190734863), (1, datetime.datetime(2023, 6, 1, 12, 0), 23.700000762939453, 23.40000057220459), (2, datetime.datetime(2023, 6, 1, 10, 0), 21.299999237060547, 21.299999237060547)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sensor temperature readings with time series analysis
conn.execute('''
    CREATE TABLE sensor_readings (
        sensor_id INT,
        reading_time TIMESTAMP,
        temperature FLOAT
    );
''')

conn.executemany('INSERT INTO sensor_readings VALUES (?, ?, ?)', [
    (1, '2023-06-01 10:00:00', 22.5),
    (1, '2023-06-01 11:00:00', 23.1),
    (1, '2023-06-01 12:00:00', 23.7),
    (2, '2023-06-01 10:00:00', 21.3)
])

# Analyze temperature trend using window functions
result = conn.execute('''
    SELECT 
        sensor_id, 
        reading_time,
        temperature,
        AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY reading_time ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg
    FROM sensor_readings
''').fetchall()

print(result)