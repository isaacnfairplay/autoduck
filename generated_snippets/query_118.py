# Generated: 2025-03-19 19:23:02.343022
# Result: [('London', 5570.22), ('Tokyo', 10851.73)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a geographic data table with point coordinates
conn.execute('''CREATE TABLE locations (
    city VARCHAR,
    latitude DOUBLE,
    longitude DOUBLE
)''')

conn.execute('''INSERT INTO locations VALUES
    ('New York', 40.7128, -74.0060),
    ('London', 51.5074, -0.1278),
    ('Tokyo', 35.6762, 139.6503)
''')

# Calculate great circle distance between points using haversine formula
result = conn.execute('''SELECT 
    city, 
    ROUND(6371 * 2 * ASIN(SQRT(
        POWER(SIN((latitude - 40.7128) * PI() / 360), 2) +
        COS(latitude * PI() / 180) * COS(40.7128 * PI() / 180) *
        POWER(SIN((longitude - (-74.0060)) * PI() / 360), 2)
    )), 2) as distance_km
FROM locations
WHERE city != 'New York'
ORDER BY distance_km''').fetchall()

for row in result:
    print(f'{row[0]}: {row[1]} km from New York')