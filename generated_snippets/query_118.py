# Generated: 2025-03-19 21:18:16.263268
# Result: [('New York', [50.0, 59.0, 68.0]), ('London', [41.0, 46.4, 53.6])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample temperature data and convert Celsius to Fahrenheit using array_transform
conn.execute('CREATE TABLE temperatures(city VARCHAR, celsius_temps INTEGER[])')
conn.execute("INSERT INTO temperatures VALUES ('New York', [10, 15, 20]), ('London', [5, 8, 12])")

result = conn.execute("""
    SELECT city, 
           array_transform(celsius_temps, x -> (x * 9/5) + 32) AS fahrenheit_temps
    FROM temperatures
""").fetchall()

print(result)