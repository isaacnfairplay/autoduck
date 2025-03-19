# Generated: 2025-03-19 11:04:02.846931
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

# Create and query a geospatial table with point data
conn = duckdb.connect(':memory:')

conn.sql('''
CREATE TABLE locations (
    id INTEGER,
    name VARCHAR,
    latitude DOUBLE,
    longitude DOUBLE
);

INSERT INTO locations VALUES
    (1, 'New York', 40.7128, -74.0060),
    (2, 'Los Angeles', 34.0522, -118.2437),
    (3, 'Chicago', 41.8781, -87.6298);

-- Calculate distance between points using Haversine formula
WITH distances AS (
    SELECT 
        l1.name AS origin,
        l2.name AS destination,
        ROUND(6371 * 2 * ASIN(
            SQRT(POW(SIN((l1.latitude - l2.latitude) * PI() / 360), 2) +
            COS(l1.latitude * PI() / 180) * COS(l2.latitude * PI() / 180) *
            POW(SIN((l1.longitude - l2.longitude) * PI() / 360), 2))
        ), 2) AS distance_km
    FROM locations l1
    CROSS JOIN locations l2
    WHERE l1.id != l2.id
)

SELECT * FROM distances ORDER BY distance_km;
''').show()