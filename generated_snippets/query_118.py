# Generated: 2025-03-19 09:02:49.887149
# Result: [('Houston', Decimal('90.10'), 1), ('Los Angeles', Decimal('85.20'), 2), ('New York', Decimal('72.50'), 3), ('Chicago', Decimal('68.30'), 4)]
# Valid: True
import duckdb

# Connect to an in-memory database
conn = duckdb.connect(':memory:')

# Create and populate a sample temperature dataset
conn.execute('CREATE TABLE weather (city TEXT, temp_f DECIMAL(5,2), recorded_at TIMESTAMP)')
conn.executemany('INSERT INTO weather VALUES (?, ?, ?)', [
    ('New York', 72.5, '2023-07-15 10:00:00'),
    ('Chicago', 68.3, '2023-07-15 11:00:00'),
    ('Los Angeles', 85.2, '2023-07-15 09:00:00'),
    ('Houston', 90.1, '2023-07-15 12:00:00')
])

# Use window function to rank cities by temperature
result = conn.execute('''
    SELECT 
        city, 
        temp_f, 
        RANK() OVER (ORDER BY temp_f DESC) as temp_rank
    FROM weather
''').fetchall()

for row in result:
    print(f"City: {row[0]}, Temperature: {row[1]}°F, Rank: {row[2]}")