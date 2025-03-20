# Generated: 2025-03-19 20:01:55.370590
# Result: (Decimal('20.08'), Decimal('45.42'))
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample temperature data
conn.execute('CREATE TABLE temperatures (city TEXT, temp DECIMAL(5,2))')
conn.executemany('INSERT INTO temperatures VALUES (?, ?)', [
    ['New York', 32.5],
    ['Chicago', 25.3],
    ['Los Angeles', 68.7],
    ['Houston', 55.2]
])

# Custom aggregate calculating temperature variance across cities
result = conn.execute('''
SELECT 
    CAST(STDDEV(temp) AS DECIMAL(5,2)) as temperature_variability,
    CAST(AVG(temp) AS DECIMAL(5,2)) as mean_temperature
FROM temperatures
''').fetchone()

print(f"Temperature Variability: {result[0]}°F, Mean: {result[1]}°F")