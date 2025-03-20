# Generated: 2025-03-19 20:02:48.997055
# Result: [('New York', 'San Francisco', 4129.09), ('New York', 'Chicago', 1144.29), ('San Francisco', 'Chicago', 2984.91)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create geospatial points table
conn.execute('CREATE TABLE locations (id INT, name TEXT, latitude FLOAT, longitude FLOAT)')
conn.executemany('INSERT INTO locations VALUES (?, ?, ?, ?)', [
    [1, 'New York', 40.7128, -74.0060],
    [2, 'San Francisco', 37.7749, -122.4194],
    [3, 'Chicago', 41.8781, -87.6298]
])

# Calculate great circle distance between cities
result = conn.execute('''
SELECT 
    l1.name as city1, 
    l2.name as city2,
    ROUND(
        6371 * 2 * ASIN(
            SQRT(
                POWER(SIN((l1.latitude - l2.latitude) * PI() / 360), 2) +
                COS(l1.latitude * PI() / 180) * COS(l2.latitude * PI() / 180) *
                POWER(SIN((l1.longitude - l2.longitude) * PI() / 360), 2)
            )
        ), 2
    ) as distance_km
FROM locations l1
CROSS JOIN locations l2
WHERE l1.id < l2.id
''').fetchall()

for row in result:
    print(f"{row[0]} to {row[1]}: {row[2]} km")