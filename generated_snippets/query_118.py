# Generated: 2025-03-19 15:47:32.537873
# Result: (7.0710678118654755, 'POINT (10 20)', 'POINT (15 25)')
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate advanced spatial query with GeoSpatial functions
conn.execute('INSTALL spatial;')
conn.execute('LOAD spatial;')

result = conn.sql('''
    WITH locations AS (
        SELECT ST_Point(10.0, 20.0) as location1,
               ST_Point(15.0, 25.0) as location2
    )
    SELECT 
        ST_Distance(location1, location2) as distance_km,
        ST_AsText(location1) as point1_text,
        ST_AsText(location2) as point2_text
    FROM locations
''').fetchone()

print(f'Distance between points: {result[0]} kilometers')