# Generated: 2025-03-19 17:25:44.224493
# Result: <duckdb.duckdb.DuckDBPyConnection object at 0x00000147DE9D6CB0>
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with geographic data
conn.execute('''CREATE TABLE cities (
    city TEXT,
    population INT,
    country TEXT,
    latitude DOUBLE,
    longitude DOUBLE
)''')

# Insert sample data
conn.execute('''INSERT INTO cities VALUES
    ('New York', 8500000, 'USA', 40.7128, -74.0060),
    ('London', 9000000, 'UK', 51.5074, -0.1278),
    ('Tokyo', 14000000, 'Japan', 35.6762, 139.6503)''')

# Perform geospatial query using haversine distance
result = conn.execute('''
    SELECT city, 
           ROUND(6371 * 2 * ASIN(SQRT(
               POWER(SIN((RADIANS(40.7128) - RADIANS(latitude)) / 2), 2) +
               COS(RADIANS(40.7128)) * COS(RADIANS(latitude)) *
               POWER(SIN((RADIANS(-74.0060) - RADIANS(longitude)) / 2), 2)
           )), 2) AS distance_km
    FROM cities
    ORDER BY distance_km
''')

print(result.fetchall())