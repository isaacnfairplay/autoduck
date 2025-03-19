# Generated: 2025-03-19 10:08:58.879616
# Result: [(1, datetime.datetime(2023, 6, 1, 10, 0), Decimal('22.50'), Decimal('23.10')), (1, datetime.datetime(2023, 6, 1, 11, 0), Decimal('23.10'), Decimal('23.10')), (2, datetime.datetime(2023, 6, 1, 10, 0), Decimal('24.30'), Decimal('24.80')), (2, datetime.datetime(2023, 6, 1, 11, 0), Decimal('24.80'), Decimal('24.80'))]
# Valid: True
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create and populate sensor temperature data
conn.execute('''
    CREATE TABLE sensor_readings (
        sensor_id INTEGER,
        timestamp TIMESTAMP,
        temperature DECIMAL(5,2)
    );
    INSERT INTO sensor_readings VALUES
        (1, '2023-06-01 10:00:00', 22.5),
        (1, '2023-06-01 11:00:00', 23.1),
        (2, '2023-06-01 10:00:00', 24.3),
        (2, '2023-06-01 11:00:00', 24.8)
''');

# Calculate max temperature per sensor with window function
result = conn.execute('''
    SELECT 
        sensor_id, 
        timestamp, 
        temperature,
        MAX(temperature) OVER (PARTITION BY sensor_id) as max_temp
    FROM sensor_readings
''').fetchall()

for row in result:
    print(row)