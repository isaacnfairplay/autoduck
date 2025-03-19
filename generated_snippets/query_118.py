# Generated: 2025-03-19 18:11:58.404466
# Result: [(datetime.datetime(2023, 6, 1, 10, 0), 'Los Angeles', 68.30000305175781, 69.0), (datetime.datetime(2023, 6, 1, 11, 0), 'Los Angeles', 69.69999694824219, 69.0), (datetime.datetime(2023, 6, 1, 10, 0), 'New York', 72.5, 73.8499984741211), (datetime.datetime(2023, 6, 1, 11, 0), 'New York', 75.19999694824219, 74.89999898274739), (datetime.datetime(2023, 6, 1, 12, 0), 'New York', 77.0, 76.0999984741211)]
# Valid: True
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create time series data with temperature measurements
conn.execute('''
    CREATE TABLE weather_data (
        timestamp TIMESTAMP,
        city VARCHAR,
        temperature FLOAT
    );

    INSERT INTO weather_data VALUES
        ('2023-06-01 10:00:00', 'New York', 72.5),
        ('2023-06-01 11:00:00', 'New York', 75.2),
        ('2023-06-01 12:00:00', 'New York', 77.0),
        ('2023-06-01 10:00:00', 'Los Angeles', 68.3),
        ('2023-06-01 11:00:00', 'Los Angeles', 69.7);
''');

# Calculate moving average of temperature with 2-hour window
result = conn.execute('''
    SELECT 
        timestamp, 
        city, 
        temperature,
        AVG(temperature) OVER (
            PARTITION BY city 
            ORDER BY timestamp 
            RANGE BETWEEN INTERVAL 1 HOUR PRECEDING AND INTERVAL 1 HOUR FOLLOWING
        ) as temperature_moving_avg
    FROM weather_data
''').fetchall()

for row in result:
    print(row)