# Generated: 2025-03-19 19:18:39.777903
# Result: [11, 12, 13, 14]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a time series table with hourly temperature readings
conn.sql("""
CREATE TABLE temperature_readings (
    timestamp TIMESTAMP,
    temperature DECIMAL(5,2)
);

INSERT INTO temperature_readings VALUES
('2023-06-01 00:00:00', 22.5),
('2023-06-01 01:00:00', 21.8),
('2023-06-01 02:00:00', 20.9),
('2023-06-01 03:00:00', 20.1);

-- Calculate rolling 2-hour average temperature
SELECT 
    timestamp, 
    temperature,
    AVG(temperature) OVER (ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS rolling_2hr_avg
FROM temperature_readings;
""")
