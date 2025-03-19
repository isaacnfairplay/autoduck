# Generated: 2025-03-19 15:54:22.391491
# Result: [('Chicago', '2023-01-01', 25, 25.0), ('Chicago', '2023-01-02', 28, 26.5), ('New York', '2023-01-01', 32, 32.0), ('New York', '2023-01-02', 35, 33.5)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample table of temperatures
conn.execute('''CREATE TABLE temperatures AS
SELECT * FROM (VALUES
    ('New York', '2023-01-01', 32),
    ('New York', '2023-01-02', 35),
    ('Chicago', '2023-01-01', 25),
    ('Chicago', '2023-01-02', 28)
) AS t(city, date, temperature)''')

# Use window function to calculate moving average
result = conn.execute('''
SELECT 
    city, 
    date, 
    temperature,
    AVG(temperature) OVER (PARTITION BY city ORDER BY date ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg
FROM temperatures
''').fetchall()

for row in result:
    print(f"City: {row[0]}, Date: {row[1]}, Temperature: {row[2]}, Moving Average: {row[3]:.2f}")