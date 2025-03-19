# Generated: 2025-03-19 18:42:46.215293
# Result: [('Chicago', datetime.date(2023, 6, 1), 68.69999694824219, None), ('Chicago', datetime.date(2023, 6, 2), 72.0999984741211, 3.4000015258789062), ('New York', datetime.date(2023, 6, 1), 75.5, None), ('New York', datetime.date(2023, 6, 2), 78.30000305175781, 2.8000030517578125)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time series data with weather patterns
conn.execute('''
    CREATE TABLE weather_data (
        date DATE,
        city VARCHAR,
        temperature FLOAT,
        precipitation FLOAT
    );

    INSERT INTO weather_data VALUES
        ('2023-06-01', 'New York', 75.5, 0.2),
        ('2023-06-02', 'New York', 78.3, 0.0),
        ('2023-06-01', 'Chicago', 68.7, 0.5),
        ('2023-06-02', 'Chicago', 72.1, 0.1)
''');

# Use window function to track temperature changes
result = conn.execute('''
    SELECT 
        city, 
        date, 
        temperature,
        temperature - LAG(temperature) OVER (PARTITION BY city ORDER BY date) as temp_change
    FROM weather_data
''').fetchall()

for row in result:
    print(f"City: {row[0]}, Date: {row[1]}, Temperature: {row[2]}, Temperature Change: {row[3] or 'N/A'}")