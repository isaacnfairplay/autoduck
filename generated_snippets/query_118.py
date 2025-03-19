# Generated: 2025-03-19 08:19:40.976092
# Result: [(1, datetime.datetime(2023, 7, 15, 10, 0), Decimal('22.50'), 22.5), (1, datetime.datetime(2023, 7, 15, 11, 0), Decimal('23.10'), 22.8), (2, datetime.datetime(2023, 7, 15, 10, 0), Decimal('21.80'), 21.8)]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create sensor temperature dataset with temporal data
conn.execute('''
CREATE TABLE sensor_readings (
    sensor_id INTEGER,
    timestamp TIMESTAMP,
    temperature DECIMAL(5,2)
);

INSERT INTO sensor_readings VALUES
    (1, '2023-07-15 10:00:00', 22.5),
    (1, '2023-07-15 11:00:00', 23.1),
    (2, '2023-07-15 10:00:00', 21.8);
''')

# Analyze temperature trends with window functions
result = conn.execute('''
SELECT
    sensor_id,
    timestamp,
    temperature,
    AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as rolling_avg
FROM sensor_readings
''').fetchall()

for row in result:
    print(row)