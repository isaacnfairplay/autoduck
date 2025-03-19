# Generated: 2025-03-19 08:29:38.445010
# Result: [('Chicago', datetime.datetime(2023, 7, 20, 10, 0), Decimal('75.80'), 75.8, None), ('New York', datetime.datetime(2023, 7, 20, 10, 0), Decimal('82.50'), 82.5, None), ('New York', datetime.datetime(2023, 7, 20, 11, 0), Decimal('83.20'), 82.85, Decimal('0.70'))]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create table with time series weather data
conn.execute('''
CREATE TABLE weather_metrics (
    city VARCHAR,
    recorded_at TIMESTAMP,
    temperature DECIMAL(5,2),
    humidity INTEGER
);

INSERT INTO weather_metrics VALUES
    ('New York', '2023-07-20 10:00:00', 82.5, 65),
    ('New York', '2023-07-20 11:00:00', 83.2, 62),
    ('Chicago', '2023-07-20 10:00:00', 75.8, 70);
''')

# Use window functions to compute temperature trends
result = conn.execute('''
SELECT
    city,
    recorded_at,
    temperature,
    AVG(temperature) OVER (PARTITION BY city ORDER BY recorded_at ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as rolling_avg,
    temperature - LAG(temperature) OVER (PARTITION BY city ORDER BY recorded_at) as temp_change
FROM weather_metrics
''').fetchall()

for row in result:
    print(row)