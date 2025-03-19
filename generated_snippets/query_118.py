# Generated: 2025-03-19 09:45:06.374155
# Result: [(1, Decimal('22.50'), 22.5, Decimal('0.00')), (2, Decimal('25.30'), 23.9, Decimal('2.80')), (3, Decimal('23.10'), 24.2, Decimal('0.60'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create geospatial sensor data table
conn.sql("""
CREATE TABLE sensor_readings (
    sensor_id INTEGER,
    latitude DOUBLE,
    longitude DOUBLE,
    temperature DECIMAL(5,2),
    timestamp TIMESTAMP
);

INSERT INTO sensor_readings VALUES
    (1, 40.7128, -74.0060, 22.5, '2023-06-15 10:30:00'),
    (2, 34.0522, -118.2437, 25.3, '2023-06-15 11:45:00'),
    (3, 41.8781, -87.6298, 23.1, '2023-06-15 12:15:00')
""")

# Analyze sensor temperature variations with window functions
result = conn.sql("""
SELECT
    sensor_id,
    temperature,
    AVG(temperature) OVER (ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as rolling_avg,
    temperature - FIRST_VALUE(temperature) OVER (ORDER BY timestamp) as temp_change
FROM sensor_readings
""").fetchall()

print(result)