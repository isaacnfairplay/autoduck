# Generated: 2025-03-19 16:58:10.144319
# Result: [('Chicago', 68.1, datetime.datetime(2023, 6, 15, 10, 0), 68.1), ('Chicago', 70.3, datetime.datetime(2023, 6, 15, 11, 0), 69.19999999999999), ('New York', 72.5, datetime.datetime(2023, 6, 15, 10, 0), 72.5), ('New York', 75.2, datetime.datetime(2023, 6, 15, 11, 0), 73.85)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create temperature readings table with geospatial and time series dimensions
conn.sql('''
CREATE TABLE weather_readings (
    city VARCHAR,
    temperature DOUBLE,
    timestamp TIMESTAMP
);

INSERT INTO weather_readings VALUES
    ('New York', 72.5, '2023-06-15 10:00:00'),
    ('New York', 75.2, '2023-06-15 11:00:00'),
    ('Chicago', 68.1, '2023-06-15 10:00:00'),
    ('Chicago', 70.3, '2023-06-15 11:00:00')
''')

# Use window function to calculate rolling temperature average
result = conn.sql('''
SELECT 
    city, 
    temperature, 
    timestamp,
    AVG(temperature) OVER (PARTITION BY city ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS rolling_avg
FROM weather_readings
''').fetchall()

print(result)