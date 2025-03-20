# Generated: 2025-03-19 21:26:05.493335
# Result: [(3, 'Chicago', 14.378673558085948)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with geospatial data and perform a nearest neighbor search
conn.execute('INSTALL spatial; LOAD spatial;')
conn.execute('CREATE TABLE locations (id INT, name VARCHAR, geom GEOMETRY)')
conn.execute("""INSERT INTO locations VALUES
    (1, 'New York', 'POINT(-74.0060 40.7128)'),
    (2, 'Los Angeles', 'POINT(-118.2437 34.0522)'),
    (3, 'Chicago', 'POINT(-87.6298 41.8781)')
""")

# Find the nearest location to a given point
result = conn.execute("""
    SELECT id, name, ST_Distance(geom, 'POINT(-95.3698 29.7604)') as distance
    FROM locations
    ORDER BY distance
    LIMIT 1
""").fetchall()

print(result)  # Should print the nearest location to Houston's coordinates