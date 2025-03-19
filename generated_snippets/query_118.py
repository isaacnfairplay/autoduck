# Generated: 2025-03-19 18:05:47.546333
# Result: [('New York', -74.006, 40.7128)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate geospatial function with PostGIS-like point manipulation
conn.execute('INSTALL spatial; LOAD spatial')
conn.execute('CREATE TABLE locations (name STRING, point GEOMETRY)')
conn.execute("INSERT INTO locations VALUES ('New York', 'POINT(-74.006 40.7128)')")

result = conn.execute("SELECT name, ST_X(point) as longitude, ST_Y(point) as latitude FROM locations").fetchall()

print(result)