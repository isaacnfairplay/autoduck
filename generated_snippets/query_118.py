# Generated: 2025-03-19 12:12:28.686795
# Result: [('New York', 10851.73306683613), ('London', 9558.561322414535), ('Tokyo', 0.00012771038834187613)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a geospatial data simulation
conn.execute('CREATE TABLE locations (id INT, name TEXT, latitude FLOAT, longitude FLOAT)')
conn.executemany('INSERT INTO locations VALUES (?, ?, ?, ?)', [
    (1, 'New York', 40.7128, -74.0060),
    (2, 'London', 51.5074, -0.1278),
    (3, 'Tokyo', 35.6762, 139.6503)
])

# Calculate distance between two points using Haversine formula
result = conn.execute('''
    SELECT 
        name, 
        2 * 6371 * ASIN(
            SQRT(
                POWER(SIN((radians(35.6762) - radians(latitude)) / 2), 2) +
                COS(radians(latitude)) * COS(radians(35.6762)) *
                POWER(SIN((radians(139.6503) - radians(longitude)) / 2), 2)
            )
        ) as distance_km
    FROM locations
''').fetchall()

print(result)