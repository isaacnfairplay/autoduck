# Generated: 2025-03-19 20:14:04.378481
# Result: [('New York', 0.0), ('Chicago', 1144.2914716113733), ('Los Angeles', 3935.7463386530785)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with geographic coordinates
conn.execute('''CREATE TABLE locations (
    city STRING,
    latitude FLOAT,
    longitude FLOAT
)''')

conn.execute('''INSERT INTO locations VALUES
    ('New York', 40.7128, -74.0060),
    ('Los Angeles', 34.0522, -118.2437),
    ('Chicago', 41.8781, -87.6298)''')

# Calculate distance between locations using Haversine formula
result = conn.execute('''SELECT
    city,
    6371 * 2 * ASIN(SQRT(
        POWER(SIN((latitude - 40.7128) * PI() / 360), 2) +
        COS(latitude * PI() / 180) * COS(40.7128 * PI() / 180) *
        POWER(SIN((longitude - (-74.0060)) * PI() / 360), 2)
    )) AS distance_km
FROM locations
ORDER BY distance_km''').fetchall()

for row in result:
    print(f"City: {row[0]}, Distance from New York: {row[1]:.2f} km")