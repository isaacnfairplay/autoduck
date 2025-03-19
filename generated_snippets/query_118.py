# Generated: 2025-03-19 08:05:48.428471
# Result: [(1, datetime.datetime(2023, 6, 1, 10, 0), Decimal('22.50'), 22.5, None), (1, datetime.datetime(2023, 6, 1, 11, 0), Decimal('23.10'), 22.8, Decimal('0.60')), (2, datetime.datetime(2023, 6, 1, 10, 0), Decimal('21.80'), 21.8, None), (2, datetime.datetime(2023, 6, 1, 11, 0), Decimal('22.30'), 22.05, Decimal('0.50'))]
# Valid: True
import duckdb

# Create an in-memory database and connect
conn = duckdb.connect(':memory:')

# Create a sensor temperature dataset with timestamps
conn.execute('''
CREATE TABLE sensor_data (
    sensor_id INTEGER,
    timestamp TIMESTAMP,
    temperature DECIMAL(5,2)
);

INSERT INTO sensor_data VALUES
    (1, '2023-06-01 10:00:00', 22.5),
    (1, '2023-06-01 11:00:00', 23.1),
    (2, '2023-06-01 10:00:00', 21.8),
    (2, '2023-06-01 11:00:00', 22.3);
''')

# Use window functions to compute rolling average and temperature change
result = conn.execute('''
SELECT 
    sensor_id, 
    timestamp,
    temperature,
    AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as rolling_avg,
    temperature - LAG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp) as temp_change
FROM sensor_data
''').fetchall()

for row in result:
    print(row)