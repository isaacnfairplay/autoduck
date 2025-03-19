# Generated: 2025-03-19 16:34:48.830792
# Result: [(1, datetime.datetime(2023, 6, 15, 10, 0), 22.5, 22.5), (1, datetime.datetime(2023, 6, 15, 11, 0), 23.100000381469727, 22.800000190734863), (2, datetime.datetime(2023, 6, 15, 10, 0), 19.799999237060547, 19.799999237060547)]
# Valid: True
import duckdb

# Create an in-memory database
conn = duckdb.connect(':memory:')

# Create a table with sensor readings
conn.execute("""
CREATE TABLE sensor_data (
    sensor_id INTEGER,
    timestamp TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT
);
""")

# Insert sample sensor data
conn.executemany("""
INSERT INTO sensor_data VALUES (?, ?, ?, ?)
""", [
    (1, '2023-06-15 10:00:00', 22.5, 45.3),
    (1, '2023-06-15 11:00:00', 23.1, 46.2),
    (2, '2023-06-15 10:00:00', 19.8, 55.7)
])

# Perform window function to calculate rolling average temperature
result = conn.execute("""
SELECT 
    sensor_id, 
    timestamp, 
    temperature,
    AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as rolling_avg_temp
FROM sensor_data
""").fetchall()

print(result)