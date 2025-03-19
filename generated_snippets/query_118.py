# Generated: 2025-03-19 14:36:22.809314
# Result: [(datetime.datetime(2023, 6, 1, 0, 0), 22.5, 22.5), (datetime.datetime(2023, 6, 1, 1, 0), 21.299999237060547, 21.899999618530273), (datetime.datetime(2023, 6, 1, 2, 0), 20.100000381469727, 20.699999809265137), (datetime.datetime(2023, 6, 1, 3, 0), 19.700000762939453, 19.90000057220459)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time series data with timestamps and temperature
conn.execute('''
CREATE TABLE weather_data (
    timestamp TIMESTAMP,
    temperature FLOAT
);

INSERT INTO weather_data VALUES
    ('2023-06-01 00:00:00', 22.5),
    ('2023-06-01 01:00:00', 21.3),
    ('2023-06-01 02:00:00', 20.1),
    ('2023-06-01 03:00:00', 19.7)
''')

# Use window functions to calculate moving average
result = conn.execute('''
SELECT 
    timestamp, 
    temperature,
    AVG(temperature) OVER (ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg
FROM weather_data
''').fetchall()

for row in result:
    print(f"Time: {row[0]}, Temp: {row[1]}, Moving Avg: {row[2]:.2f}")