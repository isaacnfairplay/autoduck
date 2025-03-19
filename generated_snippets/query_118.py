# Generated: 2025-03-19 17:03:21.496482
# Result: [(1, 'Northeast', 72.5, datetime.datetime(2023, 7, 15, 10, 0), 72.5, 74.2), (1, 'Northeast', 74.2, datetime.datetime(2023, 7, 15, 11, 0), 73.35, 74.2), (2, 'Midwest', 68.1, datetime.datetime(2023, 7, 15, 10, 0), 68.1, 70.3), (2, 'Midwest', 70.3, datetime.datetime(2023, 7, 15, 11, 0), 69.19999999999999, 70.3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create geospatial temperature tracking with multi-dimensional window analysis
conn.sql('''
CREATE TABLE weather_stations (
    station_id INT,
    region VARCHAR,
    temperature DOUBLE,
    timestamp TIMESTAMP
);

INSERT INTO weather_stations VALUES
    (1, 'Northeast', 72.5, '2023-07-15 10:00:00'),
    (1, 'Northeast', 74.2, '2023-07-15 11:00:00'),
    (2, 'Midwest', 68.1, '2023-07-15 10:00:00'),
    (2, 'Midwest', 70.3, '2023-07-15 11:00:00')
''');

# Compute complex temperature trend analysis with multiple window functions
result = conn.sql('''
SELECT 
    station_id,
    region,
    temperature,
    timestamp,
    AVG(temperature) OVER (PARTITION BY station_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS rolling_avg,
    MAX(temperature) OVER (PARTITION BY region) AS regional_max
FROM weather_stations
''').fetchall()

print(result)