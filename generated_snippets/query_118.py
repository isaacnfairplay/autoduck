# Generated: 2025-03-19 13:18:26.794191
# Result: [([32.0, 50.0, 68.0, 86.0],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Convert temperatures from Celsius to Fahrenheit in an array
result = conn.execute('SELECT array_transform([0, 10, 20, 30], x -> x * 9/5 + 32) as fahrenheit_temps').fetchall()

print(result)