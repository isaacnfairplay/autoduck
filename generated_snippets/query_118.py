# Generated: 2025-03-19 14:51:48.943764
# Result: [(datetime.datetime(2024, 1, 1, 10, 0), Decimal('22.50'), None), (datetime.datetime(2024, 1, 1, 10, 15), Decimal('23.10'), Decimal('0.60')), (datetime.datetime(2024, 1, 1, 10, 30), Decimal('21.90'), Decimal('1.20')), (datetime.datetime(2024, 1, 1, 10, 45), Decimal('22.70'), Decimal('0.80'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with sensor readings and calculate moving range
conn.execute('CREATE TABLE sensor_data (timestamp TIMESTAMP, temperature DECIMAL(5,2))')
conn.execute("INSERT INTO sensor_data VALUES ('2024-01-01 10:00:00', 22.5), ('2024-01-01 10:15:00', 23.1), ('2024-01-01 10:30:00', 21.9), ('2024-01-01 10:45:00', 22.7)")

result = conn.execute("""
SELECT 
    timestamp, 
    temperature, 
    ABS(temperature - LAG(temperature) OVER (ORDER BY timestamp)) AS temperature_change
FROM sensor_data
""").fetchall()

for row in result:
    print(f"Timestamp: {row[0]}, Temperature: {row[1]}°C, Change: {row[2]}°C")