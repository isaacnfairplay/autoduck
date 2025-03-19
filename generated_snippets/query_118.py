# Generated: 2025-03-19 14:06:58.056229
# Result: [('San Francisco', 'New York', 48.502499986459924), ('Chicago', 'New York', 13.667293421681741), ('New York', 'San Francisco', 48.502499986459924), ('Chicago', 'San Francisco', 35.03776591025019), ('New York', 'Chicago', 13.667293421681741), ('San Francisco', 'Chicago', 35.03776591025019)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create geospatial data table with point coordinates
conn.execute('''
CREATE TABLE locations (
    city TEXT,
    latitude DECIMAL(8,6),
    longitude DECIMAL(9,6)
);

INSERT INTO locations VALUES
    ('New York', 40.712776, -74.005974),
    ('San Francisco', 37.774929, -122.419418),
    ('Chicago', 41.881832, -87.623177);
''')

# Query to calculate distance between cities
result = conn.execute('''
SELECT 
    l1.city as city1, 
    l2.city as city2,
    SQRT(POWER(l1.latitude - l2.latitude, 2) + POWER(l1.longitude - l2.longitude, 2)) as approximate_distance
FROM locations l1
CROSS JOIN locations l2
WHERE l1.city != l2.city
''').fetchall()

for row in result:
    print(row)