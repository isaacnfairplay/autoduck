# Generated: 2025-03-19 16:23:16.317549
# Result: [4, 9, 16, 25]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate time series data
conn.execute('''
    CREATE TABLE sensor_readings (
        timestamp TIMESTAMP,
        sensor_id INT,
        temperature FLOAT
    );

    INSERT INTO sensor_readings VALUES
        ('2023-01-01 10:00:00', 1, 22.5),
        ('2023-01-01 10:15:00', 1, 23.1),
        ('2023-01-01 10:30:00', 1, 22.8),
        ('2023-01-01 10:00:00', 2, 21.7),
        ('2023-01-01 10:15:00', 2, 21.9);

    -- Use window function to calculate rolling average
    WITH rolling_temp AS (
        SELECT
            sensor_id,
            timestamp,
            temperature,
            AVG(temperature) OVER (
                PARTITION BY sensor_id
                ORDER BY timestamp
                ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
            ) as rolling_avg
        FROM sensor_readings
    )
    SELECT * FROM rolling_temp;
''').fetchall()