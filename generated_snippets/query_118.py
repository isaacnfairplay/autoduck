# Generated: 2025-03-19 11:04:55.187018
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and analyze sensor performance data
conn.sql('''
CREATE TABLE sensor_readings (
    sensor_id INTEGER,
    reading_time TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT
);

INSERT INTO sensor_readings VALUES
    (1, '2023-01-01 10:00:00', 22.5, 45.3),
    (1, '2023-01-01 11:00:00', 23.1, 46.2),
    (2, '2023-01-01 10:00:00', 19.8, 55.7),
    (2, '2023-01-01 11:00:00', 20.3, 54.9);

-- Calculate moving average and standard deviation of temperature
SELECT
    sensor_id,
    reading_time,
    temperature,
    AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY reading_time ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS moving_avg,
    STDDEV(temperature) OVER (PARTITION BY sensor_id) AS temperature_variation
FROM sensor_readings
''').show()